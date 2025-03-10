import { mount } from '@vue/test-utils'
import NotFound from '@/views/NotFound.vue'
import Content from '@/components/Content.vue'

describe('NotFound.vue', () => {
  it('renders the Content component', () => {
    const wrapper = mount(NotFound)
    expect(wrapper.findComponent(Content).exists()).toBe(true)
  })

  it('displays 404 message', () => {
    const wrapper = mount(NotFound)
    expect(wrapper.text()).toContain('404')
  })
})