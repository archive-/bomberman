# require File.join(File.dirname(__FILE__), 'step_helper.rb')

When /^I run the program$/ do
  @client = Client.new
end

Then /^the client should appear on the screen$/ do
  @client.window != nil
end
