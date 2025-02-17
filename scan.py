from subprocess import getoutput
import time
DEBUG = False

print("DEBUG: ", DEBUG)
cmd = "cargo fmt && cargo build"
if not DEBUG:
    cmd += " -r"
ret = getoutput(cmd)
dt_max = 0
dt_max_i = 0
score_min = -1
score_min_i = 0
score_max = -1
score_max_i = 0
score_sum = 0
norm = 0
with open("score1.csv", "w") as f:
    for i in range(100):
        print(i, end = ":")
        cmd = "cargo run"
        if not DEBUG:
            cmd += " -r"
        cmd += " < tools/in/{0:04d}.txt > tools/out/{0:04d}.txt".format(i, i)
        t0 = time.time()
        ret = getoutput(cmd)
        t1 = time.time()
        score = int(ret.split()[-1])
        dt = int(1000 * (t1 - t0))
        if dt_max < dt:
            dt_max = dt
            dt_max_i = i
        if score_min < 0 or score_min > score:
            score_min = score
            score_min_i = i
        if score_max < 0 or score_max < score:
            score_max = score
            score_max_i = i
        score_sum += score
        norm += 1
        print(score, dt, score,
            "score_min", score_min, score_min_i,
            "score_max", score_max, score_max_i,
            "time_max", dt_max, dt_max_i)
        f.write("{}\n".format(score))
print(score_sum / norm)