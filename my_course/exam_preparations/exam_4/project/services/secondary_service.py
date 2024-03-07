from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=15)

    def details(self):
        result = f'{self.name} Secondary Service:\nRobots:'
        if not self.robots:
            result += ' none'
        else:
            robots = [r.name for r in self.robots]
            for r in robots:
                result += f' {r}'

        return result
