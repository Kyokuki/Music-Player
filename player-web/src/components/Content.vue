<template>
    <div class="container">
      <div class="card">
        <div class="card-body">
            <slot></slot>
        </div>
      </div>
    </div>
</template>

<script>
export default{
    name:"Content",
}
</script>

<style scoped>
.card{
  margin-top: 20px;
  flex: 1; /* 占满剩余空间 */
  margin-bottom: 10px; /* 内容区域的内边距 */
}
</style>