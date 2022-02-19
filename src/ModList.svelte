<script lang="ts">
    import Mod from "./Mod.svelte";


    export let singleModId: number | null;
    export let modList;
</script>

{#each modList as mod (mod.modId)}
    <Mod {mod} bind:singleModId/>
{:else}
    <article class="message is-info">
        <div class="message-body">
            No results.
        </div>
    </article>
{/each}
