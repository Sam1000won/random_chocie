from src.project.choice import pick_presenter, main

def test_pick_presenter():
    members = ["1", "2", "3", "4", "5"]
    presenter = pick_presenter(members)
    assert presenter in members

def test_main(monkeypatch):
    inputs = ["1", "2", "q"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    main()