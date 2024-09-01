<script>
  import { Label, Fileupload } from 'flowbite-svelte';

  let fileuploadprops = {
    id: 'user_avatar'
  };

  let fileuploadprops2 = {
    id: 'user_avatar2'
  };
</script>

<Label class="pb-2">Upload file</Label>
<Fileupload {...fileuploadprops} />
