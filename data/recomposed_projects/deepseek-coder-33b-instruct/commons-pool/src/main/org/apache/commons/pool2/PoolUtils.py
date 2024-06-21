from __future__ import annotations
import io
import threading
import typing
from typing import *
import os
from src.main.org.apache.commons.pool2.KeyedObjectPool import *
from src.main.org.apache.commons.pool2.KeyedPooledObjectFactory import *
from src.main.org.apache.commons.pool2.ObjectPool import *
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.PooledObject import *


class ErodingFactor:

    __idleHighWaterMark: int = None
    __nextShrinkMillis: int = None
    __factor: float = None

    def toString(self) -> str:

        return (
            "ErodingFactor{"
            + "factor="
            + str(self.__factor)
            + ", idleHighWaterMark="
            + str(self.__idleHighWaterMark)
            + "}"
        )

    def update(self, nowMillis: int, numIdle: int) -> None:

        idle = max(0, numIdle)
        self.__idleHighWaterMark = max(idle, self.__idleHighWaterMark)
        maxInterval = 15.0
        minutes = maxInterval + ((1.0 - maxInterval) / self.__idleHighWaterMark) * idle
        self.__nextShrinkMillis = nowMillis + int((minutes * 60000.0 * self.__factor))

    def getNextShrink(self) -> int:

        return self.__nextShrinkMillis

    def __init__(self, factor: float) -> None:

        self.__factor = factor
        self.__nextShrinkMillis = int(time.time() * 1000) + (900000 * factor)
        self.__idleHighWaterMark = 1


class ErodingKeyedObjectPool(KeyedObjectPool):

    __erodingFactor: ErodingFactor = None
    __keyedPool: KeyedObjectPool[typing.Any, typing.Any] = None

    def toString(self) -> str:

        return (
            "ErodingKeyedObjectPool{"
            + "factor="
            + str(self.__erodingFactor)
            + ", keyedPool="
            + str(self.__keyedPool)
            + "}"
        )

    def returnObject(self, key: typing.Any, obj: typing.Any) -> None:

        discard = False
        nowMillis = int(round(time.time() * 1000))
        factor = self._getErodingFactor(key)

        with self.__keyedPool:
            if factor.getNextShrink() < nowMillis:
                numIdle = self.getNumIdle1(key)
                if numIdle > 0:
                    discard = True

                factor.update(nowMillis, numIdle)

        try:
            if discard:
                self.__keyedPool.invalidateObject0(key, obj)
            else:
                self.__keyedPool.returnObject(key, obj)
        except Exception as e:
            pass

    def invalidateObject0(self, key: typing.Any, obj: typing.Any) -> None:

        try:
            self.__keyedPool.invalidateObject0(key, obj)
        except Exception as e:
            pass

    def close(self) -> None:

        try:
            self.__keyedPool.close()
        except Exception as e:
            pass

    def borrowObject(self, key: typing.Any) -> typing.Any:

        return self.__keyedPool.borrowObject(key)

    def addObject(self, key: typing.Any) -> None:

        self.__keyedPool.addObject(key)

    def getNumIdle1(self, key: typing.Any) -> int:

        return self.__keyedPool.getNumIdle1(key)

    def getNumIdle0(self) -> int:

        return self.__keyedPool.getNumIdle0()

    def getNumActive1(self, key: typing.Any) -> int:

        return self.__keyedPool.getNumActive1(key)

    def getNumActive0(self) -> int:

        return self.__keyedPool.getNumActive0()

    def _getKeyedPool(self) -> KeyedObjectPool[typing.Any, typing.Any]:

        return self.__keyedPool

    def _getErodingFactor(self, key: typing.Any) -> ErodingFactor:

        return self.__erodingFactor

    def clear1(self, key: typing.Any) -> None:

        try:
            self.__keyedPool.clear1(key)
        except Exception as e:
            raise e
        except NotImplementedError as uoe:
            raise uoe

    def clear0(self) -> None:

        try:
            self.__keyedPool.clear0()
        except Exception as e:
            raise e
        except NotImplementedError as uoe:
            raise uoe

    @staticmethod
    def ErodingKeyedObjectPool0(
        keyedPool: KeyedObjectPool[typing.Any], factor: float
    ) -> ErodingKeyedObjectPool[typing.Any]:

        return ErodingKeyedObjectPool(keyedPool, factor)

    def __init__(
        self,
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        erodingFactor: ErodingFactor,
    ) -> None:

        if keyedPool is None:
            raise ValueError(MSG_NULL_KEYED_POOL)

        self.__keyedPool = keyedPool
        self.__erodingFactor = erodingFactor


class ErodingObjectPool(ObjectPool):

    __factor: ErodingFactor = None
    __pool: ObjectPool[typing.Any] = None

    def toString(self) -> str:

        return (
            "ErodingObjectPool{factor="
            + str(self.__factor)
            + ", pool="
            + str(self.__pool)
            + "}"
        )

    def returnObject(self, obj: typing.Any) -> None:

        discard = False
        nowMillis = int(round(time.time() * 1000))
        with self.__pool:
            if self.__factor.getNextShrink() < nowMillis:
                numIdle = self.__pool.getNumIdle()
                if numIdle > 0:
                    discard = True

                self.__factor.update(nowMillis, numIdle)

        try:
            if discard:
                self.__pool.invalidateObject0(obj)
            else:
                self.__pool.returnObject(obj)
        except Exception as e:
            pass

    def invalidateObject0(self, obj: typing.Any) -> None:

        try:
            self.__pool.invalidateObject0(obj)
        except Exception as e:
            pass

    def getNumIdle(self) -> int:

        if self.__pool is None:
            return 0

        return self.__pool.getNumIdle()

    def getNumActive(self) -> int:

        if self.__pool is None:
            return 0

        return self.__pool.getNumActive()

    def close(self) -> None:

        try:
            self.__pool.close()
        except Exception as e:
            pass

    def clear(self) -> None:

        try:
            self.__pool.clear()
        except Exception as e:
            raise e
        except NotImplementedError as uoe:
            raise uoe

    def borrowObject(self) -> typing.Any:

        try:
            return self.__pool.borrowObject()
        except Exception as e:
            raise e
        except NoSuchElementException as e:
            raise e
        except IllegalStateException as e:
            raise e

    def addObject(self) -> None:

        try:
            self.__pool.addObject()
        except Exception as e:
            print(f"Exception occurred: {e}")
            raise
        except IllegalStateException as e:
            print(f"IllegalStateException occurred: {e}")
            raise
        except NotImplementedError as e:
            print(f"NotImplementedError occurred: {e}")
            raise

    def __init__(self, pool: ObjectPool[typing.Any], factor: float) -> None:

        self.__pool = pool
        self.__factor = ErodingFactor(factor)


class ErodingPerKeyKeyedObjectPool:

    __factors: typing.Dict[typing.Any, ErodingFactor] = typing.cast(
        typing.Dict[typing.Any, ErodingFactor], collections.synchronized(dict())
    )
    __factor: float = None

    def toString(self) -> str:

        return (
            "ErodingPerKeyKeyedObjectPool{"
            + "factor="
            + str(self.__factor)
            + ", keyedPool="
            + str(self.getKeyedPool())
            + "}"
        )

    def _getErodingFactor(self, key: typing.Any) -> ErodingFactor:

        eFactor = self.__factors.get(key)
        if eFactor is None:
            eFactor = ErodingFactor(self.__factor)
            self.__factors[key] = eFactor
        return eFactor

    def __init__(
        self, keyedPool: KeyedObjectPool[typing.Any, typing.Any], factor: float
    ) -> None:

        super().__init__(keyedPool, None)
        self.__factor = factor


class KeyedObjectPoolMinIdleTimerTask:

    __keyedPool: KeyedObjectPool[typing.Any, typing.Any] = None
    __key: typing.Any = None
    __minIdle: int = None

    def toString(self) -> str:

        sb = io.StringIO()
        sb.write("KeyedObjectPoolMinIdleTimerTask")
        sb.write("{minIdle=").write(str(self.__minIdle))
        sb.write(", key=").write(str(self.__key))
        sb.write(", keyedPool=").write(str(self.__keyedPool))
        sb.write("}")
        return sb.getvalue()

    def run(self) -> None:

        success = False
        try:
            if self.__keyedPool.getNumIdle1(self.__key) < self.__minIdle:
                self.__keyedPool.addObject(self.__key)
            success = True

        except Exception as e:
            self.cancel()

        finally:
            if not success:
                self.cancel()

    def __init__(
        self,
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        key: typing.Any,
        minIdle: int,
    ) -> None:

        if keyedPool is None:
            raise ValueError(MSG_NULL_KEYED_POOL)

        self.__keyedPool = keyedPool
        self.__key = key
        self.__minIdle = minIdle


class ObjectPoolMinIdleTimerTask:

    __pool: ObjectPool[typing.Any] = None
    __minIdle: int = None

    def toString(self) -> str:

        sb = io.StringIO()
        sb.write("ObjectPoolMinIdleTimerTask")
        sb.write("{minIdle=")
        sb.write(str(self.__minIdle))
        sb.write(", pool=")
        sb.write(str(self.__pool))
        sb.write("}")
        return sb.getvalue()

    def run(self) -> None:

        success = False
        try:
            if self.__pool.getNumIdle() < self.__minIdle:
                self.__pool.addObject()
            success = True

        except Exception as e:
            self.cancel()
        finally:
            if not success:
                self.cancel()

    def __init__(self, pool: ObjectPool[typing.Any], minIdle: int) -> None:

        if pool is None:
            raise ValueError(MSG_NULL_POOL)

        self.__pool = pool
        self.__minIdle = minIdle


class SynchronizedKeyedObjectPool(KeyedObjectPool):

    __keyedPool: KeyedObjectPool[typing.Any, typing.Any] = None

    __readWriteLock: threading.RLock = threading.RLock()

    def toString(self) -> str:

        sb = "SynchronizedKeyedObjectPool"
        sb += "{keyedPool=" + str(self.__keyedPool) + "}"
        return sb

    def returnObject(self, key: typing.Any, obj: typing.Any) -> None:

        writeLock = self.__readWriteLock.writeLock()
        writeLock.acquire()
        try:
            self.__keyedPool.returnObject(key, obj)
        except Exception as e:
            pass
        finally:
            writeLock.release()

    def invalidateObject0(self, key: typing.Any, obj: typing.Any) -> None:

        writeLock = self.__readWriteLock.acquire()
        try:
            self.__keyedPool.invalidateObject0(key, obj)
        except Exception as e:
            pass
        finally:
            self.__readWriteLock.release()

    def close(self) -> None:

        writeLock = self.__readWriteLock.writeLock()
        writeLock.acquire()
        try:
            self.__keyedPool.close()
        except Exception as e:
            pass
        finally:
            writeLock.release()

    def borrowObject(self, key: typing.Any) -> typing.Any:

        writeLock = self.__readWriteLock.writeLock()
        writeLock.acquire()
        try:
            return self.__keyedPool.borrowObject(key)
        finally:
            writeLock.release()

    def addObject(self, key: typing.Any) -> None:

        writeLock = self.__readWriteLock.acquire()
        try:
            self.__keyedPool.addObject(key)
        finally:
            writeLock.release()

    def getNumIdle1(self, key: typing.Any) -> int:

        readLock = self.__readWriteLock.acquire()
        try:
            return self.__keyedPool.getNumIdle1(key)
        finally:
            self.__readWriteLock.release()

    def getNumIdle0(self) -> int:

        self.__readWriteLock.acquire()
        try:
            return self.__keyedPool.getNumIdle0()
        finally:
            self.__readWriteLock.release()

    def getNumActive1(self, key: typing.Any) -> int:

        readLock = self.__readWriteLock.acquire()
        try:
            return self.__keyedPool.getNumActive1(key)
        finally:
            self.__readWriteLock.release()

    def getNumActive0(self) -> int:

        self.__readWriteLock.acquire()
        try:
            return self.__keyedPool.getNumActive0()
        finally:
            self.__readWriteLock.release()

    def clear1(self, key: typing.Any) -> None:

        writeLock = self.__readWriteLock.acquire()
        try:
            self.__keyedPool.clear1(key)
        finally:
            writeLock.release()

    def clear0(self) -> None:

        writeLock = self.__readWriteLock.acquire()
        try:
            self.__keyedPool.clear0()
        finally:
            writeLock.release()

    def __init__(self, keyedPool: KeyedObjectPool[typing.Any, typing.Any]) -> None:

        if keyedPool is None:
            raise ValueError(MSG_NULL_KEYED_POOL)

        self.__keyedPool = keyedPool


class SynchronizedKeyedPooledObjectFactory:

    __keyedFactory: KeyedPooledObjectFactory[typing.Any, typing.Any] = None

    __writeLock: typing.Union[threading.RLock, threading.Lock] = threading.Lock()

    def validateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> bool:

        self.__writeLock.acquire()
        try:
            return self.__keyedFactory.validateObject(key, p)
        finally:
            self.__writeLock.release()

    def toString(self) -> str:

        sb = io.StringIO()
        sb.write("SynchronizedKeyedPoolableObjectFactory")
        sb.write("{keyedFactory=")
        sb.write(str(self.__keyedFactory))
        sb.write("}")
        return sb.getvalue()

    def ivateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:

        self.__writeLock.acquire()
        try:
            self.__keyedFactory.passivateObject(key, p)
        finally:
            self.__writeLock.release()

    def makeObject(self, key: typing.Any) -> PooledObject[typing.Any]:

        self.__writeLock.acquire()
        try:
            return self.__keyedFactory.makeObject(key)
        finally:
            self.__writeLock.release()

    def destroyObject0(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:

        self.__writeLock.acquire()
        try:
            self.__keyedFactory.destroyObject0(key, p)
        finally:
            self.__writeLock.release()

    def activateObject(self, key: typing.Any, p: PooledObject[typing.Any]) -> None:

        self.__writeLock.acquire()
        try:
            self.__keyedFactory.activateObject(key, p)
        finally:
            self.__writeLock.release()

    def __init__(
        self, keyedFactory: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> None:

        if keyedFactory is None:
            raise ValueError("keyedFactory must not be null.")

        self.__keyedFactory = keyedFactory


class SynchronizedObjectPool(ObjectPool):

    __pool: ObjectPool[typing.Any] = None

    __readWriteLock: threading.RLock = threading.RLock()

    def toString(self) -> str:

        sb = io.StringIO()
        sb.write("SynchronizedObjectPool")
        sb.write("{pool=")
        sb.write(str(self.__pool))
        sb.write("}")
        return sb.getvalue()

    def returnObject(self, obj: typing.Any) -> None:

        writeLock = self.__readWriteLock.acquire()
        try:
            self.__pool.returnObject(obj)
        except Exception as e:
            pass
        finally:
            writeLock.release()

    def invalidateObject0(self, obj: typing.Any) -> None:

        writeLock = self._readWriteLock.acquire_write()
        try:
            self._pool.invalidateObject0(obj)
        except Exception as e:
            pass
        finally:
            writeLock.release()

    def getNumIdle(self) -> int:

        self.__readWriteLock.acquire()
        try:
            return self.__pool.getNumIdle()
        finally:
            self.__readWriteLock.release()

    def getNumActive(self) -> int:

        self.__readWriteLock.acquire()
        try:
            return self.__pool.getNumActive()
        finally:
            self.__readWriteLock.release()

    def close(self) -> None:

        writeLock = self.__readWriteLock.writeLock()
        writeLock.acquire()
        try:
            self.__pool.close()
        except Exception as e:
            pass
        finally:
            writeLock.release()

    def clear(self) -> None:

        writeLock = self.__readWriteLock.writeLock()
        writeLock.acquire()
        try:
            self.__pool.clear()
        finally:
            writeLock.release()

    def borrowObject(self) -> typing.Any:

        writeLock = self.__readWriteLock.acquire()
        try:
            return self.__pool.borrowObject()
        finally:
            writeLock.release()

    def addObject(self) -> None:

        writeLock = self.__readWriteLock.acquire()
        try:
            self.__pool.addObject()
        finally:
            writeLock.release()

    def __init__(self, pool: ObjectPool[typing.Any]) -> None:

        if pool is None:
            raise ValueError(MSG_NULL_POOL)
        self.__pool = pool


class SynchronizedPooledObjectFactory:

    __factory: PooledObjectFactory[typing.Any] = None

    __writeLock: typing.Union[threading.RLock, threading.Lock] = threading.Lock()

    def validateObject(self, p: PooledObject[typing.Any]) -> bool:

        self.__writeLock.acquire()
        try:
            return self.__factory.validateObject(p)
        finally:
            self.__writeLock.release()

    def toString(self) -> str:

        sb = io.StringIO()
        sb.write("SynchronizedPoolableObjectFactory")
        sb.write("{factory=")
        sb.write(str(self.__factory))
        sb.write("}")
        return sb.getvalue()

    def ivateObject(self, p: PooledObject[typing.Any]) -> None:

        self.__writeLock.acquire()
        try:
            self.__factory.passivateObject(p)
        finally:
            self.__writeLock.release()

    def makeObject(self) -> PooledObject[typing.Any]:

        self.__writeLock.acquire()
        try:
            return self.__factory.makeObject()
        finally:
            self.__writeLock.release()

    def destroyObject0(self, p: PooledObject[typing.Any]) -> None:

        self.__writeLock.acquire()
        try:
            self.__factory.destroyObject0(p)
        finally:
            self.__writeLock.release()

    def activateObject(self, p: PooledObject[typing.Any]) -> None:

        self.__writeLock.acquire()
        try:
            self.__factory.activateObject(p)
        finally:
            self.__writeLock.release()

    def __init__(self, factory: PooledObjectFactory[typing.Any]) -> None:

        if factory is None:
            raise ValueError("factory must not be null.")

        self.__factory = factory


class TimerHolder:

    MIN_IDLE_TIMER: threading.Timer = threading.Timer(0, None)


class PoolUtils:

    MSG_NULL_KEYS: str = "keys must not be null."

    MSG_NULL_KEY: str = "key must not be null."

    __MSG_NULL_POOL: str = "pool must not be null."

    __MSG_NULL_KEYED_POOL: str = "keyedPool must not be null."

    __MSG_MIN_IDLE: str = "minIdle must be non-negative."

    __MSG_FACTOR_NEGATIVE: str = "factor must be positive."

    @staticmethod
    def prefill2(pool: ObjectPool[typing.Any], count: int) -> None:

        if pool is None:
            raise ValueError(PoolUtils.__MSG_NULL_POOL)
        pool.addObjects(count)

    @staticmethod
    def prefill1(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any], key: typing.Any, count: int
    ) -> None:

        if keyedPool is None:
            raise ValueError(PoolUtils.__MSG_NULL_KEYED_POOL)

        keyedPool.addObjects1(key, count)

    @staticmethod
    def prefill0(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        keys: typing.Collection[typing.Any],
        count: int,
    ) -> None:

        if keys is None:
            raise ValueError(PoolUtils.MSG_NULL_KEYS)

        keyedPool.addObjects0(keys, count)

    def __init__(self) -> None:

        pass

    @staticmethod
    def synchronizedPooledFactory(
        factory: PooledObjectFactory[typing.Any],
    ) -> PooledObjectFactory[typing.Any]:

        class SynchronizedPooledObjectFactory(PooledObjectFactory[typing.Any]):
            def __init__(self, factory: PooledObjectFactory[typing.Any]):
                self.factory = factory
                self.lock = threading.Lock()

            def activateObject(self, pooledObject: PooledObject[typing.Any]) -> None:
                with self.lock:
                    self.factory.activateObject(pooledObject)

            def destroyObject(self, pooledObject: PooledObject[typing.Any]) -> None:
                with self.lock:
                    self.factory.destroyObject(pooledObject)

            def makeObject(self) -> PooledObject[typing.Any]:
                with self.lock:
                    return self.factory.makeObject()

            def passivateObject(self, pooledObject: PooledObject[typing.Any]) -> None:
                with self.lock:
                    self.factory.passivateObject(pooledObject)

            def validateObject(self, pooledObject: PooledObject[typing.Any]) -> bool:
                with self.lock:
                    return self.factory.validateObject(pooledObject)

        return SynchronizedPooledObjectFactory(factory)

    @staticmethod
    def synchronizedPool1(pool: ObjectPool[typing.Any]) -> ObjectPool[typing.Any]:

        if pool is None:
            raise ValueError(PoolUtils.__MSG_NULL_POOL)

        return SynchronizedObjectPool(pool)

    @staticmethod
    def synchronizedPool0(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any]
    ) -> KeyedObjectPool[typing.Any, typing.Any]:

        class SynchronizedKeyedObjectPool(KeyedObjectPool[typing.Any, typing.Any]):
            def __init__(self, keyedPool: KeyedObjectPool[typing.Any, typing.Any]):
                self.keyedPool = keyedPool
                self.lock = threading.Lock()

            def borrowObject(self, key: typing.Any) -> typing.Any:
                with self.lock:
                    return self.keyedPool.borrowObject(key)

            def returnObject(self, key: typing.Any, obj: typing.Any) -> None:
                with self.lock:
                    self.keyedPool.returnObject(key, obj)

            def invalidateObject(self, key: typing.Any, obj: typing.Any) -> None:
                with self.lock:
                    self.keyedPool.invalidateObject(key, obj)

            def addObject(self, key: typing.Any) -> None:
                with self.lock:
                    self.keyedPool.addObject(key)

            def clear(self) -> None:
                with self.lock:
                    self.keyedPool.clear()

            def close(self) -> None:
                with self.lock:
                    self.keyedPool.close()

        return SynchronizedKeyedObjectPool(keyedPool)

    @staticmethod
    def synchronizedKeyedPooledFactory(
        keyedFactory: KeyedPooledObjectFactory[typing.Any, typing.Any]
    ) -> KeyedPooledObjectFactory[typing.Any, typing.Any]:

        class SynchronizedKeyedPooledObjectFactory(
            KeyedPooledObjectFactory[typing.Any, typing.Any]
        ):
            def __init__(
                self, keyedFactory: KeyedPooledObjectFactory[typing.Any, typing.Any]
            ):
                self.keyedFactory = keyedFactory
                self.lock = threading.Lock()

            def activateObject(
                self, key: typing.Any, obj: PooledObject[typing.Any]
            ) -> None:
                with self.lock:
                    self.keyedFactory.activateObject(key, obj)

            def destroyObject(
                self, key: typing.Any, obj: PooledObject[typing.Any]
            ) -> None:
                with self.lock:
                    self.keyedFactory.destroyObject(key, obj)

            def makeObject(self, key: typing.Any) -> PooledObject[typing.Any]:
                with self.lock:
                    return self.keyedFactory.makeObject(key)

            def passivateObject(
                self, key: typing.Any, obj: PooledObject[typing.Any]
            ) -> None:
                with self.lock:
                    self.keyedFactory.passivateObject(key, obj)

            def validateObject(
                self, key: typing.Any, obj: PooledObject[typing.Any]
            ) -> bool:
                with self.lock:
                    return self.keyedFactory.validateObject(key, obj)

        return SynchronizedKeyedPooledObjectFactory(keyedFactory)

    @staticmethod
    def erodingPool4(
        pool: ObjectPool[typing.Any], factor: float
    ) -> ObjectPool[typing.Any]:

        if pool is None:
            raise ValueError(PoolUtils.__MSG_NULL_POOL)
        if factor <= 0:
            raise ValueError(PoolUtils.__MSG_FACTOR_NEGATIVE)
        return ErodingObjectPool(pool, factor)

    @staticmethod
    def erodingPool3(pool: ObjectPool[typing.Any]) -> ObjectPool[typing.Any]:

        return PoolUtils.erodingPool4(pool, 1.0)

    @staticmethod
    def erodingPool2(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any], factor: float, perKey: bool
    ) -> KeyedObjectPool[typing.Any, typing.Any]:

        if keyedPool is None:
            raise ValueError(PoolUtils.__MSG_NULL_KEYED_POOL)
        if factor <= 0.0:
            raise ValueError(PoolUtils.__MSG_FACTOR_NEGATIVE)
        if perKey:
            return ErodingPerKeyKeyedObjectPool(keyedPool, factor)
        return PoolUtils.ErodingKeyedObjectPool0(keyedPool, factor)

    @staticmethod
    def erodingPool1(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any], factor: float
    ) -> KeyedObjectPool[typing.Any, typing.Any]:

        return PoolUtils.erodingPool2(keyedPool, factor, False)

    @staticmethod
    def erodingPool0(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any]
    ) -> KeyedObjectPool[typing.Any, typing.Any]:

        return PoolUtils.erodingPool1(keyedPool, 1.0)

    @staticmethod
    def checkRethrow(t: BaseException) -> None:

        if isinstance(t, threading.ThreadDeath):
            raise t
        if isinstance(t, MemoryError):
            raise t

    @staticmethod
    def checkMinIdle2(
        pool: ObjectPool[typing.Any], minIdle: int, periodMillis: int
    ) -> typing.Union[sched.scheduler, threading.Timer]:

        if pool is None:
            raise ValueError(PoolUtils.__MSG_NULL_KEYED_POOL)
        if minIdle < 0:
            raise ValueError(PoolUtils.__MSG_MIN_IDLE)
        task = ObjectPoolMinIdleTimerTask(pool, minIdle)
        PoolUtils.__getMinIdleTimer().schedule(task, 0, periodMillis)
        return task

    @staticmethod
    def checkMinIdle1(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        key: typing.Any,
        minIdle: int,
        periodMillis: int,
    ) -> typing.Union[sched.scheduler, threading.Timer]:

        if keyedPool is None:
            raise ValueError(PoolUtils.MSG_NULL_KEYED_POOL)
        if key is None:
            raise ValueError(PoolUtils.MSG_NULL_KEY)
        if minIdle < 0:
            raise ValueError(PoolUtils.MSG_MIN_IDLE)
        task = KeyedObjectPoolMinIdleTimerTask(keyedPool, key, minIdle)
        PoolUtils.__getMinIdleTimer().schedule(task, 0, periodMillis)
        return task

    @staticmethod
    def checkMinIdle0(
        keyedPool: KeyedObjectPool[typing.Any, typing.Any],
        keys: typing.Collection[typing.Any],
        minIdle: int,
        periodMillis: int,
    ) -> typing.Dict[typing.Any, typing.Union[sched.scheduler, threading.Timer]]:

        if keys is None:
            raise ValueError(PoolUtils.MSG_NULL_KEYS)

        tasks: typing.Dict[
            typing.Any, typing.Union[sched.scheduler, threading.Timer]
        ] = {}
        iterator = iter(keys)

        while True:
            try:
                key = next(iterator)
            except StopIteration:
                break

            task = PoolUtils.checkMinIdle1(keyedPool, key, minIdle, periodMillis)
            tasks[key] = task

        return tasks

    @staticmethod
    def __getMinIdleTimer() -> threading.Timer:

        return TimerHolder.MIN_IDLE_TIMER
