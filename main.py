import asyncio
from typing import Callable

from auth import login
from utils import menus


async def show_user_menu() -> Callable:
    """
    All functionalities of the user
    :return:
    """
    print(menus.user_menu)
    # return show_user_menu()


async def show_admin_menu() -> Callable:
    """
    All functionalities of the admin
    :return:
    """
    print(menus.admin_menu)
    # return show_admin_menu()


async def show_auth_menu() -> Callable | None:
    """
    Show auth menu
    :return: function based on option
    """
    print(menus.auth_menu)
    option = input("Enter your option: ")
    if option == "1":
        await login.register()

    elif option == "2":
        user_type = await login.login()
        if user_type == "admin":
            return await show_admin_menu()
        elif user_type == "user":
            return await show_user_menu()

    elif option == "3":
        print("Good bye")
        return None

    return await show_auth_menu()


if __name__ == '__main__':
    # create tables in here
    # execute_query(query=models.users)

    asyncio.run(show_auth_menu())
