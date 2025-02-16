from subprocess import getoutput
import time
cmd = "cargo fmt && cargo build -r"
ret = getoutput(cmd)
dt_max = 0
for i in range(100):
    print(i, end = ":")
    cmd = "cargo run -r < tools/in/{0:04d}.txt > tools/out/{0:04d}.txt".format(i, i)
    t0 = time.time()
    ret = getoutput(cmd)
    score = int(ret.split()[-1])
    t1 = time.time()
    dt = int(1000 * (t1 - t0))
    if dt_max < dt:
        dt_max = dt
    print(score, dt, dt_max)