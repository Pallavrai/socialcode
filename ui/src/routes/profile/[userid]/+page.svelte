<script lang="ts">
	export let data: {userid: string}
	import { onMount } from 'svelte';

	

	onMount(async () => {
	let data: any = null;
	const response = await fetch('http://127.0.0.1:8000/api/profiles');
	data = await response.json();
	console.log(data);
	});
</script>

<h3>
	Profile for user {data.userid}
</h3>
