<script lang="ts">
    export let method: string = '';
    export let label: string = '';
    export let direction: string = '';
    $: selected = (label.toLowerCase() === method);

    const callback = () => {
        if(selected){
            direction = direction === 'ASC' ? 'DESC' : 'ASC';
        } else {
            direction = 'DESC';
            method = label.toLowerCase();
        }
    }
</script>

{#if selected}
    <button class="button is-primary is-selected" on:click={callback}>
        {label} <span class="tag is-white is-rounded">{direction}</span>
    </button>
{:else}
    <button class="button" on:click={callback}>
        {label}
    </button>
{/if}

<style>
    .tag {margin-left: .5em;}
</style>
