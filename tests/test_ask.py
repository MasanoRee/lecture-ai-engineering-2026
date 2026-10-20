import builtins
import sys
from types import SimpleNamespace
from unittest.mock import Mock, call

from app import ask as ask_module
from app.config import MODEL


def test_main_reuses_chat_for_follow_up_questions(monkeypatch, capsys):
    chat = Mock()
    chat.send_message.side_effect = [
        SimpleNamespace(
            text="最初の回答",
            usage_metadata=SimpleNamespace(
                prompt_token_count=3,
                candidates_token_count=5,
            ),
        ),
        SimpleNamespace(text="続きの回答", usage_metadata=None),
    ]
    client = SimpleNamespace(chats=SimpleNamespace(create=Mock(return_value=chat)))
    client_factory = Mock(return_value=client)
    monkeypatch.setattr(ask_module.genai, "Client", client_factory)
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "test-key")
    monkeypatch.setattr(sys, "argv", ["app.ask", "最初の質問"])
    monkeypatch.setattr(builtins, "input", Mock(side_effect=["追加質問", ""]))

    ask_module.main()

    client_factory.assert_called_once_with(api_key="test-key")
    client.chats.create.assert_called_once_with(model=MODEL)
    chat.send_message.assert_has_calls([call("最初の質問"), call("追加質問")])
    output = capsys.readouterr().out
    assert "最初の回答" in output
    assert "続きの回答" in output
    assert "[usage] input_tokens=3 output_tokens=5" in output