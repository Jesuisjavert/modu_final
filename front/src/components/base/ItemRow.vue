<template>
    <v-container fill-height grid-list-md text-xs-center>
        <v-layout row wrap align-center>
            <v-col align="center" justify="center">
                <slot />
            </v-col>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    name: "ItemRow",
}
</script>

<style>

</style>