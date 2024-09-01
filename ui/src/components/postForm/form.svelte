<script lang="ts">
     import { Section } from "flowbite-svelte-blocks"
     import { Label, Button, Textarea, Fileupload } from "flowbite-svelte"
     import { CameraPhotoSolid } from "flowbite-svelte-icons"
     import { onDestroy } from "svelte"
     import axios from "axios"
     import { goto } from "$app/navigation"

     let file: File | null = null
     let previewUrl: string | null = null
     let err: string | undefined = undefined

     const handleFileChange = (event: Event) => {
          const target = event.target as HTMLInputElement
          if (target.files && target.files[0]) {
               file = target.files[0]
               previewUrl = URL.createObjectURL(file)
          } else {
               file = null
               previewUrl = null
          }
     }

     const handleSubmit = async (event: Event) => {
          event.preventDefault()
          if (!file) {
               alert("Please select a file to upload.")
               return
          }
          const formData = new FormData()
          formData.append(
               "",
               (document.getElementById("description") as HTMLTextAreaElement)
                    .value
          )
          formData.append("file", file)
          try {
               const response = await axios.post(
                    `${import.meta.env.VITE_PUBLIC_API_URL}/posts`,
                    {
                         body: formData,
                    }
               )
               if (response.status === 200) {
                    goto("/")
               }
          } catch (error) {
               console.error("Error submitting the form:", error)
               err = error.message as string
          }
     }

     onDestroy(() => {
          if (previewUrl) {
               URL.revokeObjectURL(previewUrl)
          }
     })
</script>

<Section name="crudcreateform">
     <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white">
          <CameraPhotoSolid size={"xl"} />
          <span class="text-primary-500 text-5xl">Create</span> a new post
     </h2>
     {#if err !== undefined}
          <span class="text-red-300">{err}</span>
     {/if}
     <form on:submit={handleSubmit}>
          <div>
               <Label for="file-upload" class="mb-2">Upload Image</Label>
               <div class="upload flex flex-col gap-2">
                    {#if previewUrl}
                         <div class="flex items-center justify-center w-full">
                              <div class="mt-4">
                                   <!-- svelte-ignore a11y-img-redundant-alt -->
                                   <img
                                        src={previewUrl}
                                        alt="Image Preview"
                                        class="max-w-full max-h-md rounded-lg"
                                   />
                              </div>
                         </div>
                    {/if}
                    <div class="flex items-center justify-center">
                         <div class="w-1/2">
                              {#if !previewUrl}
                                   <Fileupload
                                        id="file-upload"
                                        accept="image/*"
                                        on:change={handleFileChange}
                                   />
                              {/if}
                         </div>
                    </div>
               </div>
               <div class="sm:col-span-2">
                    <Label for="description" class="mb-2">Description</Label>
                    <Textarea
                         id="description"
                         placeholder="Add a short description about this post"
                         rows="4"
                         name="description"
                         required
                    />
               </div>
               <div class="w-full mt-2">
                    <Button type="submit" class="w-full">Post</Button>
               </div>
          </div>
     </form>
</Section>
