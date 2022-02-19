<script lang="ts">
    import SorterButton from "./SorterButton.svelte";

    export let method: string;
    export let direction: string;
</script>

<div class="buttons has-addons is-right">
    <button class="button" disabled>Order by</button>
    <SorterButton bind:method label="Created" bind:direction/>
    <SorterButton bind:method label="Updated" bind:direction/>
    <SorterButton bind:method label="Downloads" bind:direction/>
</div>
