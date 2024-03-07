from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=30)

    def details(self):
        result = f'{self.name} Main Service:\nRobots:'
        if not self.robots:
            result += ' none'
        else:
            robots = [r.name for r in self.robots]
            for r in robots:
                result += f' {r}'

        return result
