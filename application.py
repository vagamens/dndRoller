#!/bin/env python2

import pygtk
pygtk.require('2.0')
import gtk

class DnDRoller():
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False

	def __init__(self):
		# Create the window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVLE)

		# Connect the delete_event to the window
		self.window.connect("delete_event", self.delete_event)
		self.window.set_border_width(10)

		# Create a vertical box to pack the horizontal boxes
		mainVBox = gtk.VBox(False, 0)
		diceVBox = gtk.VBox(False, 0)
		resultsVBox = gtk.VBox(False, 0)
		# Create the horizontal boxes
		mainRow = gtk.HBox(False, 0)
		labelRow = gtk.HBox(False, 0)
		buttonRow = gtk.HBox(False, 0)
		d4Row = gtk.HBox(False, 0)
		d6Row = gtk.HBox(False, 0)
		d8Row = gtk.HBox(False, 0)
		d10Row = gtk.HBox(False, 0)
		d12Row = gtk.HBox(False, 0)
		d20Row = gtk.HBox(False, 0)
		d100Row = gtk.HBox(False, 0)
		dxRow = gtk.HBox(False, 0)

		# Initialize the top row labels
		dieLabel = gtk.Label("Die")
		numberLabel = gtk.Label("Number")
		addSubLabel = gtk.Label("+ -")
		resultsLabel = gtk.Label("Results")
		# Set the alignment for the labels
		dielabel.set_alignment(0, 0)
		numberLabel.set_alignment(0, 0)
		addSubLabel.set_alignment(0, 0)
		resultsLabel.set_alignment(0, 0)
		# Pack the labels into the horizontal box
		labelRow.pack_start(dieLabel, False, False, 0)
		labelRow.pack_start(numberLabel, False, False, 0)
		labelRow.pack_start(addSubLabel, False, False, 0)
		labelRow.pack_start(resultsLabel, False, False, 0)
		# Show the labels
		dieLabel.show()
		numberLabel.show()
		addSubLabel.show()
		resultsLabel.show()

		# Pack the label row into its vertical box
		mainVBox.pack_start(labelRow, False, False, 0)

def main():
	gtk.main()
	return 0

if __name__ == '__main__':
	main()