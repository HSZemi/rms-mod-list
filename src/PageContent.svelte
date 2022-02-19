<script lang="ts">
    import FilterInput from "./FilterInput.svelte";
    import Messages from "./Messages.svelte";
    import ModList from "./ModList.svelte";
    import SingleMod from "./SingleMod.svelte";
    import type {IMod} from "./Interfaces";
    import Sorter from "./Sorter.svelte";
    import {filter, singleModId, sortDirection, sortMethod} from "./stores";

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

    export let modList: IMod[];
    $: filteredModList = filtered(modList, $filter);
    $: sortedModList = sort(filteredModList, $sortMethod, $sortDirection);
</script>

<section class="section">
    <div class="container">
        <Messages {modList}/>
        {#if $singleModId}
            <SingleMod {modList}/>
        {:else}
            <div class="columns is-desktop">
                <div class="column is-three-fifths-widescreen">
                    <FilterInput filteredCount={sortedModList.length}/>
                </div>
                <div class="column">
                    <Sorter/>
                </div>
            </div>
            <ModList modList={sortedModList}/>
        {/if}
    </div>
</section>