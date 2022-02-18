<script lang="ts">
    export let filter = '';

</script>

<div class="columns">
    <div class="column ">
        <input class="input is-rounded" type="text" id="filter" placeholder="Filter..." bind:value={filter}>
    </div>
</div>
