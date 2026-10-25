from types import SimpleNamespace

from app import ask as ask_module


def test_ask_displays_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=34,
        ),
        text="回答",
    )
    client = SimpleNamespace(
        models=SimpleNamespace(generate_content=lambda **_: response)
    )
    monkeypatch.setattr(ask_module.genai, "Client", lambda **_: client)

    assert ask_module.ask("質問") == "回答"
    assert capsys.readouterr().out == "[usage] 入力トークン数: 12, 出力トークン数: 34\n"
