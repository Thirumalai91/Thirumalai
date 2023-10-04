from datetime import datetime

# Device class
class Device:
    def __init__(self, device_id, device_type, status=None, temperature=None):
        self.device_id = device_id
        self.device_type = device_type
        self.status = status
        self.temperature = temperature

    def __str__(self):
        if self.device_type == 'light':
            return f'Light {self.device_id} is {self.status}'
        elif self.device_type == 'thermostat':
            return f'Thermostat is set to {self.temperature} degrees'
        elif self.device_type == 'door':
            return f'Door is {self.status}'

# Schedule class
class Schedule:
    def __init__(self, device_id, time, command):
        self.device_id = device_id
        self.time = time
        self.command = command

    def __str__(self):
        return f'Schedule for Device {self.device_id} at {self.time}: {self.command}'

# Trigger class
class Trigger:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def __str__(self):
        return f'Trigger on condition: {self.condition} will perform action: {self.action}'

# HomeAutomationSystem class
class HomeAutomationSystem:
    def __init__(self):
        self.devices = {}
        self.schedules = []
        self.triggers = []

    def add_device(self, device_id, device_type, status=None, temperature=None):
        device = Device(device_id, device_type, status, temperature)
        self.devices[device_id] = device

    def turn_on(self, device_id):
        if device_id in self.devices:
            self.devices[device_id].status = 'On'

    def turn_off(self, device_id):
        if device_id in self.devices:
            self.devices[device_id].status = 'Off'

    def set_schedule(self, device_id, time, command):
        self.schedules.append(Schedule(device_id, time, command))

    def add_trigger(self, condition, action):
        self.triggers.append(Trigger(condition, action))

    def status_report(self):
        for device_id, device in self.devices.items():
            print(device)

    def execute_schedules(self):
        current_time = datetime.now().strftime("%H:%M")
        for schedule in self.schedules:
            if schedule.time == current_time:
                command = schedule.command.replace(f'({schedule.device_id})', f'({schedule.device_id})')
                eval(f'self.{command}')

    def execute_triggers(self):
        for trigger in self.triggers:
            condition = trigger.condition.replace('>', ' > ')
            action = trigger.action.replace('(', ' (')
            if eval(condition):
                eval(f'self.{action}')

if __name__ == "__main__":
    home = HomeAutomationSystem()

    # Adding devices
    home.add_device(1, 'light', 'Off')
    home.add_device(2, 'thermostat', temperature=70)
    home.add_device(3, 'door', 'Locked')

    # Executing commands
    home.turn_on(1)
    home.set_schedule(2, "06:00", "turn_on(2)")
    home.add_trigger("temperature > 75", "turn_off(1)")

    # Printing status report
    home.status_report()

    # Executing schedules and triggers
    home.execute_schedules()
    home.execute_triggers()
