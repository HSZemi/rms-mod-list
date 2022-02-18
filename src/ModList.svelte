<script lang="ts">
    import LoadingProgress from "./LoadingProgress.svelte";
    import Mod from "./Mod.svelte";
    import type {IMod} from "./Interfaces";

    export let singleModId: number | null;
    export let filter = '';
    export let modList: IMod[];
    $: filteredModList = modList ? modList.filter(mod => (mod.modName + '|' + mod.modDescription).toLowerCase().indexOf(filter.toLowerCase()) > -1) : [];
</script>

{#if modList}
    {#each filteredModList as mod (mod.modId)}
        <Mod {mod} bind:singleModId/>
    {:else}
        <article class="message is-info">
            <div class="message-body">
                No results.
            </div>
        </article>
    {/each}
{:else}
    <LoadingProgress/>
{/if}