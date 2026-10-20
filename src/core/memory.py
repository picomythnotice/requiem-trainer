from __future__ import annotations

from dataclasses import dataclass

import pymem
import pymem.process


@dataclass
class ProcessMemory:
    pid: int
    _pm: pymem.Pymem

    @classmethod
    def attach(cls, process_name: str) -> "ProcessMemory":
        pm = pymem.Pymem(process_name)
        return cls(pid=pm.process_id, _pm=pm)

    def read_int(self, address: int) -> int:
        return self._pm.read_int(address)

    def write_int(self, address: int, value: int) -> None:
        self._pm.write_int(address, value)

    def read_float(self, address: int) -> float:
        return self._pm.read_float(address)

    def write_float(self, address: int, value: float) -> None:
        self._pm.write_float(address, value)

    def write_bytes(self, address: int, data: bytes) -> None:
        self._pm.write_bytes(address, data, len(data))

    def base_module(self, module: str = "re_requiem.exe") -> int:
        return pymem.process.module_from_name(self._pm.process_handle, module).lpBaseOfDll