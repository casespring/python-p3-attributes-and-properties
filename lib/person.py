#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name: str, job: str):
        self._name = None
        self._job = None
        self.set_name = name
        self.set_job = job

    @property
    def set_name(self):
        return self._name
    
    @set_name.setter
    def set_name(self, name):
        if len(name) < 1 or len(name) > 25:
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = name

    @property
    def set_job(self):
        return self._job
    
    @set_job.setter
    def set_job(self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = job
