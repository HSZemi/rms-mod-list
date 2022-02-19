<script lang="ts">
    import {sortDirection, sortMethod} from "./stores";

    export let label: string = '';
    $: selected = (label.toLowerCase() === $sortMethod);

    const callback = () => {
        if(selected){
            sortDirection.update(direction => (direction === 'ASC' ? 'DESC' : 'ASC'));
        } else {
            sortDirection.set('DESC');
            sortMethod.set(label.toLowerCase());
        }
    }
</script>

{#if selected}
    <button class="button is-primary is-selected" on:click={callback}>
        {label} <span class="tag is-white is-rounded">{$sortDirection}</span>
    </button>
{:else}
    <button class="button" on:click={callback}>
        {label}
    </button>
{/if}

<style>
    .tag {margin-left: .5em;}
</style>
