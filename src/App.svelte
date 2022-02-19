<script lang="ts">
	import Header from "./Header.svelte";
	import PageContent from "./PageContent.svelte";
	import Footer from "./Footer.svelte";
	import LoadingProgress from "./LoadingProgress.svelte";
	import {resetTitleAndUrl, updateTitleAndUrl} from "./helpers";
	import {onDestroy} from "svelte";
	import {singleModId} from "./stores";
	import LoadingError from "./LoadingError.svelte";


	const unsubscribe = singleModId.subscribe(value => {
		if (value) {
			updateTitleAndUrl(value);
		} else {
			resetTitleAndUrl();
		}
	});

	onDestroy(unsubscribe);


	const init = async (filename) => {
		const response = await fetch(filename);
		const json = await response.json();

		if (response.ok) {
			let modList = json.modList;
			let lastUpdate = json.lastUpdate;
			let modCount = json.modList.length
			return {modList, lastUpdate, modCount};
		} else {
			throw new Error("Fetching mods failed");
		}
	};

	let promise: Promise<{ modList, lastUpdate, modCount }> = init("/data/all_the_maps.json");

</script>

<main>
	<Header {promise}/>
	{#await promise}
		<LoadingProgress/>
	{:then resolved}
		<PageContent modList={resolved.modList}/>
	{:catch error}
		<LoadingError/>
	{/await}
	<Footer/>
</main>
