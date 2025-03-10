import { mount } from '@vue/test-utils'
import Content from '@/components/Content.vue'

describe('Content.vue', () => {
  it('renders slot content', () => {
    const wrapper = mount(Content, {
      slots: {
        default: 'Test content'
      }
    })
    expect(wrapper.text()).toContain('Test content')
  })

  it('has the correct CSS classes', () => {
    const wrapper = mount(Content)
    expect(wrapper.find('.container').exists()).toBe(true)
    expect(wrapper.find('.card').exists()).toBe(true)
    expect(wrapper.find('.card-body').exists()).toBe(true)
  })
})