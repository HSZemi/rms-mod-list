<script lang="ts">
    import FilterInput from "./FilterInput.svelte";
    import Messages from "./Messages.svelte";
    import ModList from "./ModList.svelte";
    import SingleMod from "./SingleMod.svelte";
    import type {IMod} from "./Interfaces";
    import Sorter from "./Sorter.svelte";

    const sort = (list: IMod[], method: string, direction: string) => {
        let key = 'createDate';
        if (method === 'updated') {
            key = 'lastUpdate';
        } else if (method === 'downloads') {
            key = 'downloads';
        }

        let trueValue = 1;
        let falseValue = -1;

        if (direction === 'DESC') {
            trueValue *= -1;
            falseValue *= -1;
        }

        return list.sort((a: IMod, b: IMod) => a[key] > b[key] ? trueValue : falseValue);
    }

    const filtered = (list: IMod[], filter: string) => {
        if (list) {
            return list.filter(mod => {
                const contentString = mod.modName + '|' + mod.creatorName + '|' + mod.modDescription;
                return contentString.toLowerCase().indexOf(filter.toLowerCase()) > -1
            });
        } else {
            return [];
        }
    }

    let filter = '';
    export let singleModId: number | null;
    export let modList: IMod[];
    $: filteredModList = filtered(modList, filter);

    let method: string = 'created';
    let direction: string = 'DESC';
    $: sortedModList = sort(filteredModList, method, direction);
</script>

<section class="section">
    <div class="container">
        <Messages {modList} bind:singleModId/>
        {#if singleModId}
            <SingleMod {modList} bind:singleModId/>
        {:else}
            <div class="columns is-desktop">
                <div class="column is-three-fifths-widescreen">
                    <FilterInput filteredCount={sortedModList.length} bind:filter/>
                </div>
                <div class="column">
                    <Sorter bind:method bind:direction/>
                </div>
            </div>
            <ModList modList={sortedModList} bind:singleModId/>
        {/if}
    </div>
</section>