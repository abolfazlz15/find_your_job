from rest_framework.response import Response


def response(*, data: dict | list | None | str = None, status: int, error: str | None = None):
    success = status < 400

    return Response(
        data={
            "data": data,
            "success": success,
            "error": error,
        },
        status=status,
    )