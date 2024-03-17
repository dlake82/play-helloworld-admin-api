# accounts/views.py
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import TokenError
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class LoginView(TokenObtainPairView):
    # TokenObtainPairView 의 response 는 refresh, access 토큰 정보를 반환하기 때문에
    # "login success" 로 바꾸고 토큰은 쿠키에 담아서 응답.
    def post(self, request: Request, *args, **kwargs) -> Response:
        res = super().post(request, *args, **kwargs)

        response = Response({"detail": "login success"}, status=status.HTTP_200_OK)
        response.set_cookie("refresh", res.data.get("refresh", None), httponly=True)
        response.set_cookie("access", res.data.get("access", None), httponly=True)

        return response


class RefreshView(TokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            refresh_token = request.COOKIES.get("refresh", "Token is not provided.")
            data = {"refresh": refresh_token}
            serializer = self.get_serializer(data=data)

            try:
                serializer.is_valid(raise_exception=True)
            except TokenError as e:
                raise ValidationError(e.args[0])

            token = serializer.validated_data
            print(token)
            response = Response(
                {"detail": "refresh success"}, status=status.HTTP_200_OK
            )
            response.set_cookie("access", token["access"], httponly=True)
            return response
        except Exception as e:
            # 토큰 만료 시간이 지났을 때
            return Response(
                {"detail": "Refresh token isn't valid."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class LogoutView(TokenBlacklistView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request: Request, *args, **kwargs) -> Response:
        refresh_token = request.COOKIES.get("refresh", "Token is not provided.")
        data = {"refresh": str(refresh_token)}
        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise ValidationError(e.args[0])

        response = Response({"detail": "token blacklisted"}, status=status.HTTP_200_OK)
        response.delete_cookie("refresh")
        response.delete_cookie("access")

        return response
