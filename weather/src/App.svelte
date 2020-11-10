<script>
	export let data = {	description: "Loading" };
	async function go() {
		const res = await fetch('http://127.0.0.1:4867/');
		data = await res.json();
	}
	go()
	// I hate those robotic text. If there is only someway to make them humane.
</script>

<main>
	<div class="a">
		<textarea>{JSON.stringify(data)}</textarea>
	</div>
	<div class="b">
		<legend>Temperature</legend>
		<div class="value">{data.temperature}°F</div>
	</div>
	<div class="c">
		<legend>Humidity</legend>
		<div class="value">{data.humidity}%</div>
	</div>
	<div class="d">
		<div class="todo">TODO: place hand-drawn weather icons here</div>
	</div>
	<div class="e">
		<legend><a href={`https://www.openstreetmap.org/#map=16/${data.latitude}/${data.longitude}`}>View Larger Map</a></legend>
		<iframe title="Map" src={`https://www.openstreetmap.org/export/embed.html?bbox=${data.longitude-0.005}%2C${data.latitude-0.005}%2C${data.longitude+0.005}%2C${data.latitude+0.005}`}></iframe>
	</div>
	<div class="f">
		<legend>Today's weather is</legend>
		<div class="value">{data.description}</div>
	</div>
	<div class="g">
		<div class="todo">TODO: human-level analysis. Need emotional engine to complete.</div>
	</div>
	<div class="i">
		<legend>Latitude</legend>
		<div class="value">{String(data.latitude).replace('-', '−')}</div>
	</div>
	<div class="j">
		<legend>Longitude</legend>
		<div class="value">{String(data.longitude).replace('-', '−')}</div>
	</div>
	<div class="k">
		<legend>Location</legend>
		<div class="value">
			{data.continent || '‐'}
			{data.country || '‐'}
			{data.state || '‐'}
			{data.county || '‐'}
			{data.city || '‐'}
			{data.zipcode || '‐'}
		</div>
	</div>
	<div class="l">
		<legend>IP Address</legend>
		<div class="value">{data.ip_address}</div>
	</div>
	<div class="m">
		<legend>Automated System</legend>
		<div class="todo">TODO: draw nearby BGP peers</div>
		<div class="value">AS {data.asn}<br>{data.as_name}</div>
	</div>
</main>

<style>
/* font */
@import url('https://fonts.googleapis.com/css2?family=Crimson+Text&family=Lato&display=swap');

main {
	display: grid;
	grid-template:
		"a b c d" 1fr
		"e f f g" 2fr
		"e i j g" 1fr
		"e k k g" 1fr
		"e l l g" 1fr
		"m m m g" 2fr
		/ 2.5fr 1fr 1fr 4fr;
	width: 100%;
	height: 100%;
}
main > div {
	border: dashed 1pt grey;
	min-width: 0;
	min-height: 0;
	position: relative;
}
legend {
	position: absolute;
	font: 12pt 'Lato', sans-serif;
	text-align: center;
	width: 100%;
	box-sizing: border-box;
}
.value {
	display: flex;
	font: 32pt 'Crimson Text', serif;
	height: 100%;
	box-sizing: border-box;
	align-items: center;
	justify-content: center;
	text-align: center;
	line-height: 1;
}
legend + .value {
	padding-top: 1rem;
}
.todo {
	position: absolute;
	width: 100%;
	box-sizing: border-box;
	padding: 1em;
	text-align: right;
	color: grey;
}

.a { grid-area: a; }
.a textarea { 
	resize: none;
	font: 8pt monospace;
	width: 100%; height: 100%;
	word-break: break-all;
}
.b { grid-area: b; }
.c { grid-area: c; }
.d { grid-area: d; }
.e { grid-area: e; }
.e iframe {
	width: 100%;
	height: 100%;
	border: none;
}
.f { grid-area: f; }
.g { grid-area: g; }
.i { grid-area: i; }
.j { grid-area: j; }
.k { grid-area: k; }
.l { grid-area: l; }
.m { grid-area: m; }
</style>