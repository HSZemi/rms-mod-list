<script lang="ts">
	import Header from "./Header.svelte";
	import PageContent from "./PageContent.svelte";
	import Footer from "./Footer.svelte";
	import LoadingProgress from "./LoadingProgress.svelte";


	const getSingleModId = () => {
		if (window.location.pathname === '/'){
			return null;
		}
		const items = window.location.pathname.split('/');
		return parseInt(items[1]);
	}

	let lastUpdate: number;
	let modCount: number;
	let modList;
	let singleModId: number|null = getSingleModId();

	const init = (filename) => {
		fetch(filename)
				.then(response => response.json())
				.then(json => {
					modList = json.modList;
					lastUpdate = json.lastUpdate;
					modCount = json.modList.length;
				});
	};

	init("/data/all_the_maps.json");

</script>

<main>
	<Header {lastUpdate} {modCount} bind:singleModId/>
	{#if modList}
		<PageContent {modList} bind:singleModId/>
	{:else}
		<LoadingProgress/>
	{/if}
	<Footer/>
</main>
