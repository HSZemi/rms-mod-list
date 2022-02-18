<script lang="ts">
    export let downloadUrl = '';
    export let modFileSize = 0;
</script>

{#if downloadUrl.startsWith('#')}
    <span title="Sorry, could not get download URL"
          class="card-footer-item">Download ({(modFileSize / 1024 / 1024).toFixed(2)} MiB)</span>
{:else}
    <a href="{downloadUrl}" class="card-footer-item">Download ({(modFileSize / 1024 / 1024).toFixed(2)} MiB)</a>
{/if}
