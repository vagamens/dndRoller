#!/usr/bin/env python2

import pygtk
pygtk.require('2.0')
import gtk
from diceRoller import dice

class Die:
	def callback(self, widget, callback_data=None):
		if self.__variable:
			self._die.setSides(int(self._Sides.get_text()))
		tempResult = 0
		for i in range(int(self._Number.get_text())):
			tempResult += self._die.roll()
		if self._RadioAdd.get_active():
			self._Result.set_text(str(tempResult + int(self._Modifier.get_text())))
		elif self._RadioSub.get_active():
			self._Result.set_text(str(tempResult - int(self._Modifier.get_text())))


	def __init__(self, sides=2, image='', showImage=True, variable=False):
		self.__variable = variable
		self.__showImage = showImage
		if self.__variable:
			self._Sides = gtk.Entry(max=3)
			self._Sides.set_width_chars(3)
			self._Sides.set_text('1')
		elif self.__showImage:
			self._Image = gtk.Image()
			self._Image.set_from_file(image)
		# Initialize the die
		self._die = dice.Dice(sides)
		# Setup the number box
		self._Number = gtk.Entry(max=3)
		self._Number.set_width_chars(3)
		# Set the number text
		self._Number.set_text('1')
		# Set the input label
		if self.__variable:
			self._NumberLabel = gtk.Label('dx')
		else:
			self._NumberLabel = gtk.Label('d' + str(sides))
		# Radio buttons
		self._RadioAdd = gtk.RadioButton(None, "")
		self._RadioSub = gtk.RadioButton(self._RadioAdd, "")
		self._RadioBox = gtk.HButtonBox()
		self._AddLabel = gtk.Label('+')
		self._SubLabel = gtk.Label('-')
		# Button box
		self._RadioBox.pack_start(self._RadioAdd, False, False, padding=0)
		self._RadioBox.pack_start(self._AddLabel, False, False, padding=0)
		self._RadioBox.pack_start(self._RadioSub, False, False, padding=0)
		self._RadioBox.pack_start(self._SubLabel, False, False, padding=0)
		# Modifier
		self._Modifier = gtk.Entry(max=3)
		self._Modifier.set_width_chars(3)
		self._Modifier.set_text('0')
		# Roll button
		self._Roll = gtk.Button(label="Roll")
		self._Roll.connect("released", self.callback)

		# Result box
		self._Result = gtk.Entry(max=0)
		self.NumberPosition = self._Number
		self.NumberLabelPosition = self._NumberLabel
		self.AddSubPosition = self._RadioBox
		self.ModifierPosition = self._Modifier
		self.RollPosition = self._Roll
		self.ResultPosition = self._Result
		if self.__variable:
			self.ImagePosition = self._Sides
		else:
			self.ImagePosition = self._Image
		self.rowStuff = [self.ImagePosition, self.NumberPosition, self.NumberLabelPosition,
						 self.AddSubPosition, self.ModifierPosition, self.RollPosition,
						 self.ResultPosition]

	def show(self):
		if self.__variable:
			self._Sides.show()
		self._Number.show()
		self._NumberLabel.show()
		self._RadioAdd.show()
		self._RadioSub.show()
		self._AddLabel.show()
		self._SubLabel.show()
		self._RadioBox.show()
		self._Modifier.show()
		self._Roll.show()
		self._Result.show()

	def reset(self):
		if self._variable:
			self._Sides.set_text('1')
		self._Number.set_text('1')
		self._Modifier.set_text('0')
		self._Result.set_text('')
		self._RadioAdd.set_active(True)

class DnDRoller:
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False

	def tableAttach(self, attachments, top=0, bottom=1):
		start, end = 0, 1
		for attachment in attachments:
			self.mainTable.attach(attachment, left_attach=start, right_attach=end, top_attach=top,
							 bottom_attach=bottom, xoptions=gtk.SHRINK|gtk.FILL,
							 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
			start += 1
			end += 1

	def __init__(self):
		# Initialize the sets
		d4 = Die(sides=4, image='d4a.jpg', variable=False)
		d6 = Die(sides=6, image='d6a.jpg', variable=False)
		d8 = Die(sides=8, image='d8a.jpg', variable=False)
		d10 = Die(sides=10, image='d10a.jpg', variable=False)
		d12 = Die(sides=12, image='d12a.jpg', variable=False)
		d20 = Die(sides=20, image='d20a.jpg', variable=False)
		d100 = Die(sides=100, image='d100a.jpg', variable=False)
		dx = Die(sides=2, showImage=False, variable=True)
		# Create the window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		# Connect the delete_event to the window
		self.window.connect("delete_event", self.delete_event)
		self.window.set_border_width(10)

		# Create a vertical box to pack the horizontal boxes
		mainTable = gtk.Table(rows=10, columns=8, homogeneous=False)
		
		# Initialize the top row labels
		dieLabel = gtk.Label("Die")
		numberLabel = gtk.Label("Number")
		addSubLabel = gtk.Label("+ -")
		blankLabel = gtk.Label("")
		modifierlabel = gtk.Label("Modifier")
		resultsLabel = gtk.Label("Results")
		# Set the alignment for the labels
		dieLabel.set_alignment(0, 0)
		addSubLabel.set_alignment(0, 0)
		blankLabel.set_alignment(0, 0)
		resultsLabel.set_alignment(0, 0)
		# Pack the labels into the horizontal box
		mainTable.attach(dieLabel, left_attach=0, right_attach=1, top_attach=0,
						 bottom_attach=1, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(addSubLabel, left_attach=3, right_attach=4, top_attach=0,
						 bottom_attach=1, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(modifierlabel, left_attach=4, right_attach=5, top_attach=0,
						 bottom_attach=1, xoptions=gtk.FILL, yoptions=gtk.FILL,
						 xpadding=0, ypadding=0)
		mainTable.attach(blankLabel, left_attach=5, right_attach=6, top_attach=0,
						 bottom_attach=1, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(resultsLabel, left_attach=6, right_attach=7, top_attach=0,
						 bottom_attach=1, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		# Show the labels
		dieLabel.show()
		numberLabel.show()
		addSubLabel.show()
		blankLabel.show()
		resultsLabel.show()

		# Setup the d4 row
		self.tableAttach(d4.rowStuff, 1, 2)

		# Setup the d6 row
		mainTable.attach(d6.ImagePosition, left_attach=0, right_attach=1,
						 top_attach=2, bottom_attach=3, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d6.NumberPosition, left_attach=1, right_attach=2,
						 top_attach=2, bottom_attach=3, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d6.AddSubPosition, left_attach=2, right_attach=3,
						 top_attach=2, bottom_attach=3, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d6.ModifierPosition, left_attach=3, right_attach=4,
						 top_attach=2, bottom_attach=3, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d6.RollPosition, left_attach=4, right_attach=5,
						 top_attach=2, bottom_attach=3, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d6.ResultPosition, left_attach=5, right_attach=6,
						 top_attach=2, bottom_attach=3, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)

		# Setup the d8 row
		mainTable.attach(d8.ImagePosition, left_attach=0, right_attach=1,
						 top_attach=3, bottom_attach=4, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d8.NumberPosition, left_attach=1, right_attach=2,
						 top_attach=3, bottom_attach=4, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d8.AddSubPosition, left_attach=2, right_attach=3,
						 top_attach=3, bottom_attach=4, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d8.ModifierPosition, left_attach=3, right_attach=4,
						 top_attach=3, bottom_attach=4, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d8.RollPosition, left_attach=4, right_attach=5,
						 top_attach=3, bottom_attach=4, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d8.ResultPosition, left_attach=5, right_attach=6,
						 top_attach=3, bottom_attach=4, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)

		# Setup the d10 row
		mainTable.attach(d10.ImagePosition, left_attach=0, right_attach=1,
						 top_attach=4, bottom_attach=5, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d10.NumberPosition, left_attach=1, right_attach=2,
						 top_attach=4, bottom_attach=5, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d10.AddSubPosition, left_attach=2, right_attach=3,
						 top_attach=4, bottom_attach=5, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d10.ModifierPosition, left_attach=3, right_attach=4,
						 top_attach=4, bottom_attach=5, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d10.RollPosition, left_attach=4, right_attach=5,
						 top_attach=4, bottom_attach=5, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d10.ResultPosition, left_attach=5, right_attach=6,
						 top_attach=4, bottom_attach=5, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)

		# Setup the d12 row
		mainTable.attach(d12.ImagePosition, left_attach=0, right_attach=1,
						 top_attach=5, bottom_attach=6, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d12.NumberPosition, left_attach=1, right_attach=2,
						 top_attach=5, bottom_attach=6, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d12.AddSubPosition, left_attach=2, right_attach=3,
						 top_attach=5, bottom_attach=6, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d12.ModifierPosition, left_attach=3, right_attach=4,
						 top_attach=5, bottom_attach=6, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d12.RollPosition, left_attach=4, right_attach=5,
						 top_attach=5, bottom_attach=6, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d12.ResultPosition, left_attach=5, right_attach=6,
						 top_attach=5, bottom_attach=6, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)

		# Setup the d20 row
		mainTable.attach(d20.ImagePosition, left_attach=0, right_attach=1,
						 top_attach=6, bottom_attach=7, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d20.NumberPosition, left_attach=1, right_attach=2,
						 top_attach=6, bottom_attach=7, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d20.AddSubPosition, left_attach=2, right_attach=3,
						 top_attach=6, bottom_attach=7, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d20.ModifierPosition, left_attach=3, right_attach=4,
						 top_attach=6, bottom_attach=7, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d20.RollPosition, left_attach=4, right_attach=5,
						 top_attach=6, bottom_attach=7, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d20.ResultPosition, left_attach=5, right_attach=6,
						 top_attach=6, bottom_attach=7, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)

		# # Setup the d100 row
		mainTable.attach(d100.ImagePosition, left_attach=0, right_attach=1,
						 top_attach=7, bottom_attach=8, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d100.NumberPosition, left_attach=1, right_attach=2,
						 top_attach=7, bottom_attach=8, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d100.AddSubPosition, left_attach=2, right_attach=3,
						 top_attach=7, bottom_attach=8, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d100.ModifierPosition, left_attach=3, right_attach=4,
						 top_attach=7, bottom_attach=8, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d100.RollPosition, left_attach=4, right_attach=5,
						 top_attach=7, bottom_attach=8, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(d100.ResultPosition, left_attach=5, right_attach=6,
						 top_attach=7, bottom_attach=8, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)

		# # Setup the dx row
		mainTable.attach(dx.ImagePosition, left_attach=0, right_attach=1,
						 top_attach=8, bottom_attach=9, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(dx.NumberPosition, left_attach=1, right_attach=2,
						 top_attach=8, bottom_attach=9, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(dx.AddSubPosition, left_attach=2, right_attach=3,
						 top_attach=8, bottom_attach=9, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(dx.ModifierPosition, left_attach=3, right_attach=4,
						 top_attach=8, bottom_attach=9, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(dx.RollPosition, left_attach=4, right_attach=5,
						 top_attach=8, bottom_attach=9, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)
		mainTable.attach(dx.ResultPosition, left_attach=5, right_attach=6,
						 top_attach=8, bottom_attach=9, xoptions=gtk.EXPAND|gtk.FILL,
						 yoptions=gtk.SHRINK|gtk.FILL, xpadding=0, ypadding=0)

		# Show all the elements
		d4.show()
		d6.show()
		d8.show()
		d10.show()
		d12.show()
		d20.show()
		d100.show()
		dx.show()
		self.window.add(mainTable)
		mainTable.show()
		self.window.show()

def main():
	DnDRoller()
	gtk.main()
	return 0

if __name__ == '__main__':
	main()