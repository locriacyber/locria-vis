<script>
const ballr = 4;
const initSpeed = 1;
const damping = 0.999;
let ballx = 50, bally = 50;

const startingAngle = Math.random() * 2 * Math.PI;
let vx = Math.cos(startingAngle) * initSpeed, vy = Math.sin(startingAngle) * initSpeed;

function update() {
    ballx += vx;
    bally += vy;
    if (ballx < ballr && vx < 0) {
        vx = -vx;
        ballx += (ballr - ballx) * 2;
    }
    if (ballx > 100 - ballr && vx > 0) {
        vx = -vx;
        ballx -= (ballx - 100 + ballr) * 2;
    }
    if (bally < ballr && vy < 0) {
        vy = -vy;
        bally += (ballr - bally) * 2;
    }
    if (bally > 100 - ballr && vy > 0) {
        vy = -vy;
        bally -= (bally - 100 + ballr) * 2;
    }
    if (speed() > 1) {
        vx *= damping;
        vy *= damping;
    }
    requestAnimationFrame(update);
}
requestAnimationFrame(update);

export function push(ax, ay) {
    vx += ax;
    vy += ay;
}

export function speed() {
    return Math.sqrt(vx**2 + vy**2)
}
</script>

<svg width=400 height=400 viewbox="-5 -5 110 110" fill="none" stroke="black" stroke-width="0.5">
    <rect x=0 y=0 width=100 height=100/>
    <circle cx={ballx} cy={bally} r={ballr}></circle>
</svg>

<style>
svg {
    box-shadow: rgba(0,0,0, 0.3) 0 0 8px;
}
</style>