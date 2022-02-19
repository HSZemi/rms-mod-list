<script lang="ts">
    import {filter} from "./stores";

    export let filteredCount = 0;
</script>

<div class="field has-addons">
    <p class="control">
                <span class="button is-static is-rounded">
                    {filteredCount}
                </span>
    </p>
    <p class="control is-flex-grow-1">
        <input class="input is-rounded" type="text" id="filter" placeholder="Filter..." bind:value={$filter}>
    </p>
</div>
