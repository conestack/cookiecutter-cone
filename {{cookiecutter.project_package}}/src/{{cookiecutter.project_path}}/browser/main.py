from pyramid.view import view_config

@view_config(
    name="test",
    renderer="templates/test.pt"
)
def test(model, request):
    print("test")
    return {}