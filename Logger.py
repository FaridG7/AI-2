import os
class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self._clear_log_file()
            self._clear_result_log_file()

    def log(self, log_message):
        os.makedirs('./logs', exist_ok=True)
        log_file_path = './logs/log.txt'
        
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"{log_message}\n")

    def _clear_log_file(self):
        log_file_path = './logs/log.txt'
        open(log_file_path, 'w').close()

    def log_results(self, log_message):
        os.makedirs('./logs', exist_ok=True)
        log_file_path = './logs/resultLog.txt'
        
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"{log_message}\n")

    def _clear_result_log_file(self):
        log_file_path = './logs/resultLog.txt'
        open(log_file_path, 'w').close()
