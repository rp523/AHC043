from subprocess import getoutput
import time
DEBUG = False

print("DEBUG: ", DEBUG)
cmd = "cargo fmt && cargo build"
if not DEBUG:
    cmd += " -r"
ret = getoutput(cmd)
dt_max = 0
for i in range(100):
    print(i, end = ":")
    cmd = "cargo run"
    if not DEBUG:
        cmd += " -r"
    cmd += " < tools/in/{0:04d}.txt > tools/out/{0:04d}.txt".format(i, i)
    print(cmd, end = " ")
    t0 = time.time()
    ret = getoutput(cmd)
    score = int(ret.split()[-1])
    t1 = time.time()
    dt = int(1000 * (t1 - t0))
    if dt_max < dt:
        dt_max = dt
    print(score, dt, dt_max)