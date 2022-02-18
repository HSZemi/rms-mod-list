<script lang="ts">
    import FilterInput from "./FilterInput.svelte";
    import Messages from "./Messages.svelte";
    import ModList from "./ModList.svelte";
    import SingleMod from "./SingleMod.svelte";

    let filter = '';
    export let modList;
    export let singleModId: number | null;
</script>

<section class="section">
    <div class="container">
        <Messages {modList} bind:singleModId/>
        {#if singleModId}
            <SingleMod {modList} bind:singleModId/>
        {:else}
            <FilterInput bind:filter/>
            <ModList {modList} {filter} bind:singleModId/>
        {/if}
    </div>
</section>