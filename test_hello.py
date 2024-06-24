# test_hello.py
def test_output(capsys):
    import hello
    captured = capsys.readouterr()
    assert captured.out == "hello world\n" * 10
