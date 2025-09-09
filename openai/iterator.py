# This will be a coding interview conducted via Coderpad. You can review the interface for iterators in your language of choice. It can also be helpful to review generators and coroutines in languages that support it. Being familiar with how Generic types work in your language of choice will also be helpful, especially if you're picking a language (eg Go) where this is a newer feature

import json
import asyncio
import os
import pytest
import tempfile
from typing import List, TypeVar, Generic, Optional
from dataclasses import dataclass
from copy import deepcopy

T = TypeVar("T")

class IteratorInterface(Generic[T]):
    def __init__(self) -> None:
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def get_state(self):
        pass

    def set_state(self, state):
        pass

# Implement Resumable List Iterator. Write a test function that checks set_state and get_state work in all positions and error for the end of iterator is handled.

@dataclass
class ListIteratorState(Generic[T]):
    l: List[T]
    idx: int


class ListIterator(IteratorInterface[T]):
    def __init__(self, l: List[T]) -> None:
        self._list = l
        self._idx = 0

    def __next__(self) -> T:
        if self._idx >= len(self._list):
            raise StopIteration
        
        v = self._list[self._idx]
        self._idx += 1
        return v
        
    def get_state(self) -> ListIteratorState:
        return ListIteratorState(
            l=deepcopy(self._list),
            idx=self._idx,
        )

    def set_state(self, state: ListIteratorState):
        self._list = deepcopy(state.l)
        self._idx = state.idx

def test_iterator(iterator: IteratorInterface, data: List[T]):
    states = [iterator.get_state()]
    for pos, v in enumerate(iterator):
        states.append(iterator.get_state())
        assert v == data[pos], f"expected {data[pos]}; actual {v} at pos {pos}"

    with pytest.raises(StopIteration):
        next(iterator)

    for idx in range(len(states)):
        iterator.set_state(states[idx])
        assert list(iterator) == data[idx:]

    print("Test successful!")

# You're provided with a JSON file iterator, implement a resumable iterator for reading a list of JSON files.

@dataclass
class FileIteratorState:
    filename: str
    position: int


class ResumableFileIterator(IteratorInterface):
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "r", encoding="utf-8")
        self.position = 0

    def __next__(self):
        self.file.seek(self.position)
        line = self.file.readline()
        if not line:
            raise StopIteration
        self.position = self.file.tell()
        return json.loads(line)

    def get_state(self):
        return FileIteratorState(self.filename, self.position)

    def set_state(self, state: FileIteratorState):
        if self.file.name != state.filename:
            self.file.close()
            self.file = open(state.filename, "r", encoding="utf-8")
        self.position = state.position
        self.file.seek(self.position)

def fake_file(data):
    fname = tempfile.mkstemp()[1]
    with open(fname, "w", encoding="utf-8") as f:
        for r in data:
            f.write(json.dumps(r) + "\n")
    return fname

def test_file_iterator():
    data = [
        {"id": 1, "value": "a"},
        {"id": 2, "value": "b"},
        {"id": 3, "value": "c"},
    ]
    test_iterator(
        iterator=ResumableFileIterator(fake_file(data)),
        data=data
    )
    test_iterator(
        iterator=ResumableFileIterator(fake_file([])),
        data=[],
    )

@dataclass
class MultipleFileIteratorState:
    filenames: List[str]
    file_id: int
    file_iterator_state: Optional[FileIteratorState]

class MultipleResumableFileIterator(IteratorInterface):
    def __init__(self, filenames: List[str]) -> None:
        self._filenames = filenames
        self._file_id = 0
        self._file_iterator = ResumableFileIterator(self._filenames[0]) if filenames else None


    def __next__(self):
        while self._file_iterator is not None:
            try:
                return next(self._file_iterator)
            except StopIteration:
                self._file_id += 1
                if self._file_id < len(self._filenames):
                    self._file_iterator = ResumableFileIterator(self._filenames[self._file_id])
                else:
                    self._file_iterator = None
        raise StopIteration

    def get_state(self):
        return MultipleFileIteratorState(
            filenames=self._filenames,
            file_id=self._file_id,
            file_iterator_state=self._file_iterator.get_state() if self._file_iterator else None
        )

    def set_state(self, state: MultipleFileIteratorState):
        self._filenames = state.filenames
        self._file_id = state.file_id
        if state.file_iterator_state is None:
            self._file_iterator = None
        else:
            self._file_iterator = ResumableFileIterator(self._filenames[self._file_id])
            self._file_iterator.set_state(state.file_iterator_state)

def test_multiple_file_iterator():
    data1 = [
        {"id": 1, "value": "a"},
        {"id": 2, "value": "b"},
        {"id": 3, "value": "c"},
    ]
    data2 = [
        {"id": 4, "value": "a"},
        {"id": 5, "value": "b"},
    ]
    test_iterator(
        iterator=MultipleResumableFileIterator([fake_file(data1), fake_file(data2)]),
        data=data1 + data2,
    )
    test_iterator(
        iterator=MultipleResumableFileIterator([fake_file([])]),
        data=[],
    )
    test_iterator(
        iterator=MultipleResumableFileIterator([]),
        data=[],
    )
    test_iterator(
        iterator=MultipleResumableFileIterator([fake_file(data1), fake_file([]), fake_file(data2)]),
        data=data1 + data2,
    )
    test_iterator(
        iterator=MultipleResumableFileIterator([fake_file([]), fake_file(data1), fake_file(data2)]),
        data=data1 + data2,
    )

class AsyncIteratorInterface():
    def __init__(self) -> None:
        pass

    def __aiter__(self):
        return self

    async def __anext__(self):
        pass

    def get_state(self):
        pass

    def set_state(self, state):
        pass

class AsyncListIterator(AsyncIteratorInterface, Generic[T]):
    def __init__(self, l: List[T]) -> None:
        self._list = l
        self._idx = 0

    async def __anext__(self) -> T:
        await asyncio.sleep(0.01)
        if self._idx >= len(self._list):
            raise StopAsyncIteration
        
        v = self._list[self._idx]
        self._idx += 1
        return v
        
    def get_state(self) -> ListIteratorState:
        return ListIteratorState(
            l=deepcopy(self._list),
            idx=self._idx,
        )

    def set_state(self, state: ListIteratorState):
        self._list = deepcopy(state.l)
        self._idx = state.idx

async def test_async_iterator(iterator: AsyncIteratorInterface, data: List[T]):
    pos = 0
    states = [iterator.get_state()]
    async for v in iterator:
        states.append(iterator.get_state())
        assert v == data[pos], f"expected {data[pos]}; actual {v} at pos {pos}"
        pos += 1

    with pytest.raises(StopAsyncIteration):
        await anext(iterator)

    for idx in range(len(states)):
        iterator.set_state(states[idx])
        v = [x async for x in iterator]
        assert v == data[idx:], f"expected {data[idx:]}; actual {v} at pos {idx}"

    print("Test successful!")

def test_list_iterator():
    data = [2, 1, 3, 4, 5]
    test_iterator(
        iterator=ListIterator[int](data),
        data=data,
    )

async def test_async_list_iterator():
    data = [2, 1, 3, 4, 5]
    await test_async_iterator(
        iterator=AsyncListIterator[int](data),
        data=data,
    )

class AsyncMultipleResumableFileIterator(AsyncIteratorInterface):
    def __init__(self, filenames: List[str]) -> None:
        self._filenames = filenames
        self._file_id = 0
        self._file_iterator = ResumableFileIterator(self._filenames[0]) if filenames else None

    async def __anext__(self):
        if self._file_iterator is None: raise StopAsyncIteration
        while self._file_id < len(self._filenames):
            try:
                await asyncio.sleep(0.01)
                return next(self._file_iterator)
            except StopIteration:
                self._file_id += 1
                if self._file_id < len(self._filenames):
                    self._file_iterator = ResumableFileIterator(self._filenames[self._file_id])
        raise StopAsyncIteration

    def get_state(self):
        return MultipleFileIteratorState(
            filenames=self._filenames,
            file_id=self._file_id,
            file_iterator_state=self._file_iterator.get_state() if self._file_iterator else None
        )

    def set_state(self, state: MultipleFileIteratorState):
        self._filenames = state.filenames
        self._file_id = state.file_id
        if state.file_iterator_state is None:
            self._file_iterator = None
        else:
            self._file_iterator = ResumableFileIterator(self._filenames[self._file_id])
            self._file_iterator.set_state(state.file_iterator_state)

async def test_async_multiple_file_iterator():
    data1 = [
        {"id": 1, "value": "a"},
        {"id": 2, "value": "b"},
        {"id": 3, "value": "c"},
    ]
    data2 = [
        {"id": 4, "value": "a"},
        {"id": 5, "value": "b"},
    ]
    await test_async_iterator(
        iterator=AsyncMultipleResumableFileIterator([fake_file(data1), fake_file(data2)]),
        data=data1 + data2,
    )
    await test_async_iterator(
        iterator=AsyncMultipleResumableFileIterator([]),
        data=[],
    )
    await test_async_iterator(
        iterator=AsyncMultipleResumableFileIterator([fake_file(data1), fake_file([]), fake_file(data2)]),
        data=data1 + data2,
    )
    await test_async_iterator(
        iterator=AsyncMultipleResumableFileIterator([fake_file([]), fake_file(data1), fake_file(data2)]),
        data=data1 + data2,
    )

# ## Part 4: Async Iterator Implementation (15 minutes)
# 
# Convert your implementations to support asynchronous iteration using Python's async/await pattern.
# 
# **Requirements:**
# 
# - Create `AsyncIteratorInterface` with async methods
# - Implement `AsyncResumableListIterator`
# - Implement `AsyncMultipleResumableFileIterator`
# - Use proper async iteration protocols (`__aiter__`, `__anext__`)
# - Handle `StopAsyncIteration` instead of `StopIteration`
# - Add simulated async I/O delays where appropriate

if __name__ == "__main__":
    test_list_iterator()
    test_file_iterator()
    test_multiple_file_iterator()
    asyncio.run(test_async_list_iterator())
    asyncio.run(test_async_multiple_file_iterator())
