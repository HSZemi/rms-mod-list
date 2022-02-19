<script lang="ts">
    import LoadingProgress from "./LoadingProgress.svelte";
    import Mod from "./Mod.svelte";
    import type {IMod} from "./Interfaces";

    export let singleModId: number|null;
    export let modList: IMod[];
    $: filteredModList = modList ? modList.filter(mod => mod.modId === singleModId) : [];
</script>

{#if modList}
    {#each filteredModList as mod (mod.modId)}
        <Mod {mod} bind:singleModId/>
    {/each}
{:else}
    <LoadingProgress/>
{/if}