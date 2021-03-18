from basescript import BaseScript


class HelloWorld(BaseScript):
    def run(self):
        """

        :return: HelloWorld
        """
        print("Hello world")


if __name__ == '__main__':
    HelloWorld().start()
