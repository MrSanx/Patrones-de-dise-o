from __future__ import annotations
from abc import ABC, abstractmethod

class User:
    statte = None

    def __init__(self, state: State) -> None:
        self.setUser(state)

    def setUser(self, state: State):
        self.statte = state
        self.statte.user = self

    def presentState(self):
        print(f"Currently {type(self.statte).__name__}")
        
    def becomeOnline(self):
        self.statte.becomeOnline()

    def becomeOffline(self):
        self.statte.becomeOffline()

class State(ABC):
    @property
    def user(self) -> User:
        return self._elevator

    @user.setter
    def user(self, elevator: User) -> None:
        self._elevator = elevator

    @abstractmethod
    def becomeOffline(self) -> None:
        pass

    @abstractmethod
    def becomeOnline(self) -> None:
        pass



class offlineState(State):
    def becomeOffline(self) -> None:
        print("User is already offline")

    def becomeOnline(self) -> None:
        print("Loggin in")
        self.user.setUser(onlineState())


class onlineState(State):
    def becomeOnline(self) -> None:
        print("Logging out ")
        self.user.setUser(offlineState())

    def becomeOffline(self) -> None:
        print("User is already online")


if __name__ == "__main__":
    user = User(offlineState())
    user.presentState()


    user.becomeOnline()
    user.presentState()