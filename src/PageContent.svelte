<script lang="ts">
    import FilterInput from "./FilterInput.svelte";
    import Messages from "./Messages.svelte";
    import ModList from "./ModList.svelte";
    import SingleMod from "./SingleMod.svelte";
    import type {IMod} from "./Interfaces";

    let filter = '';
    export let singleModId: number | null;
    export let modList: IMod[];
    $: filteredModList = modList ? modList.filter(mod => (mod.modName + '|' + mod.modDescription).toLowerCase().indexOf(filter.toLowerCase()) > -1) : [];
</script>

<section class="section">
    <div class="container">
        <Messages {modList} bind:singleModId/>
        {#if singleModId}
            <SingleMod {modList} bind:singleModId/>
        {:else}
            <FilterInput filteredCount={filteredModList.length} bind:filter/>
            <ModList modList={filteredModList} bind:singleModId/>
        {/if}
    </div>
</section>