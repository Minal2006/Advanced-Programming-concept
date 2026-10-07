from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Password Authentication Successful")

class OTPAuthentication(Authentication):
    def authenticate(self):
        print("OTP Authentication Successful")

class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Biometric Authentication Successful")

methods = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for m in methods:
    m.authenticate()