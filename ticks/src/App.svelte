<script>
import Game from './Game.svelte'

const retention = 5000; // how long ticks are preserved
const width = 500; // svg size
const height = 200;

let game;

let ticks = new Set();
function addOne() {
	const now = Date.now();
	ticks.add(now);
	ticks = ticks;
	setTimeout(() => {
		ticks.delete(now);
		ticks = ticks;
	}, retention+100);

	const angle = now % 20 / 20 * Math.PI * 2;
	game.push(Math.cos(angle), Math.sin(angle));
}
let ticksNormalized = [];
function update() {
	const now = Date.now();
	ticksNormalized = Array.from(ticks).map(x => { return {
		raw: x,
		progress: (now - x) / retention,
		rotation: x % 20 / 20,
	}; });
	requestAnimationFrame(update);
}
requestAnimationFrame(update);
</script>

<header>
<h1>Spiking non-neural non-network!</h1>
<button tabindex=0 on:click={addOne}>Add One</button>
</header>

<main class="grid">
<div class="column">
	<h2>Ticks, tabulated</h2>
	<ol>
		{#each Array.from(ticks) as x}
			<li>{x}</li>
		{/each}
	</ol>
</div>
<div class="column">
	<h2>Ticks, visualized</h2>
	<svg width={width} height={height}>
		<line x1=0 y1={height/2} x2={width} y2={height/2} stroke="black" />
		{#each ticksNormalized as tick}
			<line x1=0 y1=-20 x2=0 y2=20 stroke="black" transform="translate({tick.progress*width}, {height/2}) rotate({20+tick.rotation*20})"/>
		{/each}
	</svg>
</div>
<div class="column utd">
	<h2>Ticks, streamlined</h2>
	<svg width=40 height=200>
		<line x1=20 y1=0 x2=20 y2=200 stroke="black" />
		{#each ticksNormalized as tick}
			<line y1=0 x1=-10 y2=0 x2=10 stroke="black" transform="translate(20, {tick.progress*200}) rotate({20+tick.rotation*20})"/>
		{/each}
	</svg>
</div>
</main>

<footer class="grid">
<div class="column">
	<h2>Bouncing ball</h2>
	<Game bind:this={game}/>
</div>
<div class="column">
	<h2>Ticks, together</h2>
	<svg width={40+100} height=400>
		<line x1={20+80} y1=0 x2={20+80} y2=400 stroke="black" />
		{#each ticksNormalized as tick}
		<g transform="translate({20+80}, {tick.progress*400}) rotate({(tick.rotation*2-1) * 10 * Math.max(1, game.speed())})">
			<line x1=-80 y1=0 x2=0 y2=0 stroke="black"/>
			<text x=30 y=0 text-anchor="end">{String(tick.raw).substr(-4)}</text>
		</g>
		{/each}
	</svg>
</div>
</footer>

<style>
header button {
	display: block;
	width: 100vw;
}
.grid {
	display: grid;
	grid-auto-columns: auto;
	grid-auto-flow: column;
	grid-template-columns: 1fr;
}
main ol {
	height: 200px;
	overflow-y: scroll;
}
.column {
	margin: 1rem;
}
.utd {
	writing-mode: vertical-rl;
}
.right {
	text-align: right;
}
</style>