<script lang="ts">
	import Header from "./Header.svelte";
	import PageContent from "./PageContent.svelte";
	import Footer from "./Footer.svelte";
	import LoadingProgress from "./LoadingProgress.svelte";
	import {resetTitleAndUrl, updateTitleAndUrl} from "./helpers";
	import {onDestroy} from "svelte";
	import {singleModId} from "./stores";


	let lastUpdate: number;
	let modCount: number;
	let modList;
	const unsubscribe = singleModId.subscribe(value => {
		if (value) {
			updateTitleAndUrl(value);
		} else {
			resetTitleAndUrl();
		}
	});

	onDestroy(unsubscribe);


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
	<Header {lastUpdate} {modCount}/>
	{#if modList}
		<PageContent {modList}/>
	{:else}
		<LoadingProgress/>
	{/if}
	<Footer/>
</main>
