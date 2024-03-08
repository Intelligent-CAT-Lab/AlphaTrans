package org.apache.commons.pool;

import java.io.File;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
    private static Engine sharedEngine;
    private static String codeDirectory = "../../../data/verified_projects/commons-pool/src/main/java/org/apache/commons/pool/";
    private static String packageDirectory = "../../../data/verified_projects/commons-pool/";
    private static Context context;
    static {
        try {
            HostAccess hostAccess = HostAccess.newBuilder(HostAccess.ALL)
.targetTypeMapping(Value.class, GenericObjectPoolConfig.class, null, (v) -> new GenericObjectPoolConfig(v))
.targetTypeMapping(Value.class, LinkedBlockingDeque.AbstractItr.class, null, (v) -> new LinkedBlockingDeque.AbstractItr(v))
.targetTypeMapping(Value.class, LinkedBlockingDeque.class, null, (v) -> new LinkedBlockingDeque(v))
.targetTypeMapping(Value.class, LinkedBlockingDeque.DescendingItr.class, null, (v) -> new LinkedBlockingDeque.DescendingItr(v))
.targetTypeMapping(Value.class, LinkedBlockingDeque.Itr.class, null, (v) -> new LinkedBlockingDeque.Itr(v))
.targetTypeMapping(Value.class, LinkedBlockingDeque.Node.class, null, (v) -> new LinkedBlockingDeque.Node(v))
.targetTypeMapping(Value.class, InterruptibleReentrantLock.class, null, (v) -> new InterruptibleReentrantLock(v))
.targetTypeMapping(Value.class, InterruptibleReentrantLock.new Consumer<Thread>(...) { ... }.class, null, (v) -> new InterruptibleReentrantLock.new Consumer<Thread>(...) { ... }(v))
.targetTypeMapping(Value.class, BaseKeyedPooledObjectFactory.class, null, (v) -> new BaseKeyedPooledObjectFactory(v))
.targetTypeMapping(Value.class, PooledSoftReference.class, null, (v) -> new PooledSoftReference(v))
.targetTypeMapping(Value.class, CallStackUtils.class, null, (v) -> new CallStackUtils(v))
.targetTypeMapping(Value.class, SecurityManagerCallStack.PrivateSecurityManager.class, null, (v) -> new SecurityManagerCallStack.PrivateSecurityManager(v))
.targetTypeMapping(Value.class, SecurityManagerCallStack.class, null, (v) -> new SecurityManagerCallStack(v))
.targetTypeMapping(Value.class, SecurityManagerCallStack.Snapshot.class, null, (v) -> new SecurityManagerCallStack.Snapshot(v))
.targetTypeMapping(Value.class, PrivateSecurityManager.new Function<Class<?>,WeakReference<Class<?>>>(...) { ... }.class, null, (v) -> new PrivateSecurityManager.new Function<Class<?>,WeakReference<Class<?>>>(...) { ... }(v))
.targetTypeMapping(Value.class, DestroyMode.class, null, (v) -> new DestroyMode(v))
.targetTypeMapping(Value.class, BasePooledObjectFactory.class, null, (v) -> new BasePooledObjectFactory(v))
.targetTypeMapping(Value.class, BaseObjectPoolConfig.class, null, (v) -> new BaseObjectPoolConfig(v))
.targetTypeMapping(Value.class, ThrowableCallStack.class, null, (v) -> new ThrowableCallStack(v))
.targetTypeMapping(Value.class, ThrowableCallStack.Snapshot.class, null, (v) -> new ThrowableCallStack.Snapshot(v))
.targetTypeMapping(Value.class, AbandonedConfig.class, null, (v) -> new AbandonedConfig(v))
.targetTypeMapping(Value.class, PoolUtils.ErodingFactor.class, null, (v) -> new PoolUtils.ErodingFactor(v))
.targetTypeMapping(Value.class, PoolUtils.class, null, (v) -> new PoolUtils(v))
.targetTypeMapping(Value.class, PoolUtils.ErodingKeyedObjectPool.class, null, (v) -> new PoolUtils.ErodingKeyedObjectPool(v))
.targetTypeMapping(Value.class, PoolUtils.ErodingObjectPool.class, null, (v) -> new PoolUtils.ErodingObjectPool(v))
.targetTypeMapping(Value.class, PoolUtils.ErodingPerKeyKeyedObjectPool.class, null, (v) -> new PoolUtils.ErodingPerKeyKeyedObjectPool(v))
.targetTypeMapping(Value.class, PoolUtils.KeyedObjectPoolMinIdleTimerTask.class, null, (v) -> new PoolUtils.KeyedObjectPoolMinIdleTimerTask(v))
.targetTypeMapping(Value.class, PoolUtils.ObjectPoolMinIdleTimerTask.class, null, (v) -> new PoolUtils.ObjectPoolMinIdleTimerTask(v))
.targetTypeMapping(Value.class, PoolUtils.SynchronizedKeyedObjectPool.class, null, (v) -> new PoolUtils.SynchronizedKeyedObjectPool(v))
.targetTypeMapping(Value.class, PoolUtils.SynchronizedKeyedPooledObjectFactory.class, null, (v) -> new PoolUtils.SynchronizedKeyedPooledObjectFactory(v))
.targetTypeMapping(Value.class, PoolUtils.SynchronizedObjectPool.class, null, (v) -> new PoolUtils.SynchronizedObjectPool(v))
.targetTypeMapping(Value.class, PoolUtils.SynchronizedPooledObjectFactory.class, null, (v) -> new PoolUtils.SynchronizedPooledObjectFactory(v))
.targetTypeMapping(Value.class, PoolUtils.TimerHolder.class, null, (v) -> new PoolUtils.TimerHolder(v))
.targetTypeMapping(Value.class, PoolImplUtils.class, null, (v) -> new PoolImplUtils(v))
.targetTypeMapping(Value.class, GenericKeyedObjectPoolConfig.class, null, (v) -> new GenericKeyedObjectPoolConfig(v))
.targetTypeMapping(Value.class, JdkProxyHandler.class, null, (v) -> new JdkProxyHandler(v))
.targetTypeMapping(Value.class, BaseGenericObjectPool.EvictionIterator.class, null, (v) -> new BaseGenericObjectPool.EvictionIterator(v))
.targetTypeMapping(Value.class, BaseGenericObjectPool.class, null, (v) -> new BaseGenericObjectPool(v))
.targetTypeMapping(Value.class, BaseGenericObjectPool.IdentityWrapper.class, null, (v) -> new BaseGenericObjectPool.IdentityWrapper(v))
.targetTypeMapping(Value.class, BaseGenericObjectPool.StatsStore.class, null, (v) -> new BaseGenericObjectPool.StatsStore(v))
.targetTypeMapping(Value.class, BaseGenericObjectPool.Evictor.class, null, (v) -> new BaseGenericObjectPool.Evictor(v))
.targetTypeMapping(Value.class, BaseGenericObjectPool.new Consumer<PooledObject<T>>(...) { ... }.class, null, (v) -> new BaseGenericObjectPool.new Consumer<PooledObject<T>>(...) { ... }(v))
.targetTypeMapping(Value.class, EvictionTimer.Reaper.class, null, (v) -> new EvictionTimer.Reaper(v))
.targetTypeMapping(Value.class, EvictionTimer.class, null, (v) -> new EvictionTimer(v))
.targetTypeMapping(Value.class, EvictionTimer.WeakRunner.class, null, (v) -> new EvictionTimer.WeakRunner(v))
.targetTypeMapping(Value.class, BaseObjectPool.class, null, (v) -> new BaseObjectPool(v))
.targetTypeMapping(Value.class, BaseObject.class, null, (v) -> new BaseObject(v))
.targetTypeMapping(Value.class, DefaultPooledObjectInfo.class, null, (v) -> new DefaultPooledObjectInfo(v))
.targetTypeMapping(Value.class, ProxiedObjectPool.class, null, (v) -> new ProxiedObjectPool(v))
.targetTypeMapping(Value.class, BaseProxyHandler.class, null, (v) -> new BaseProxyHandler(v))
.targetTypeMapping(Value.class, DefaultPooledObject.class, null, (v) -> new DefaultPooledObject(v))
.targetTypeMapping(Value.class, NoOpCallStack.class, null, (v) -> new NoOpCallStack(v))
.targetTypeMapping(Value.class, JdkProxySource.class, null, (v) -> new JdkProxySource(v))
.targetTypeMapping(Value.class, ProxiedKeyedObjectPool.class, null, (v) -> new ProxiedKeyedObjectPool(v))
.targetTypeMapping(Value.class, PooledObjectState.class, null, (v) -> new PooledObjectState(v))
.targetTypeMapping(Value.class, CglibProxySource.class, null, (v) -> new CglibProxySource(v))
.targetTypeMapping(Value.class, DefaultEvictionPolicy.class, null, (v) -> new DefaultEvictionPolicy(v))
.targetTypeMapping(Value.class, EvictionConfig.class, null, (v) -> new EvictionConfig(v))
// TODO: Add other mappings
                    .build();

            sharedEngine = Engine.create();
            context = Context.newBuilder("python")
                    .allowHostAccess(hostAccess)
                    .allowAllAccess(true)
                    .option("python.PythonPath", packageDirectory)
                    .engine(sharedEngine)
                    .build();
        } catch (Exception e) {
            System.out.println("[-] " + e);
        }
    }
    public static Value[] getPythonClasses(String fileName, String... classNames) {
        try {
            File file = new File(codeDirectory, fileName);
            Source source = Source.newBuilder("python", file).build();
            assert source != null;

            context.eval(source);

            Value[] result = new Value[classNames.length];
            for (int i = 0; i < classNames.length; i++) {
                result[i] = context.getBindings("python").getMember(classNames[i]);
            }
            return result;
        } catch (Exception e) {
            System.out.println("[-] " + e);
            return null; // ??
        }
    }
    public static Value getPythonClass(String fileName, String className) {
        return getPythonClasses(fileName, className)[0];
    }
}
