from src.controllers.interfaces.user_finder import UserFinderInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class UserFinderView:
    def __init__(self, controller: UserFinderInterface) -> None:
        self.__controller = controller
    async def handle_find_user(self, http_request: HttpRequest) -> HttpResponse:
        if http_request.path_params is None:
            return HttpResponse(
                body={"error": "Path params required"},
                status_code=400
            )

        user_name = http_request.path_params["user_name"]
        response = self.__controller.find_user(user_name)
        return HttpResponse(body=response,status_code=200)